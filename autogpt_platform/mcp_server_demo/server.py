"""MCP Server Demo

Run (stdio):
  python server.py

Run (HTTP):
  MCP_TRANSPORT=streamable-http MCP_HOST=127.0.0.1 MCP_PORT=8800 python server.py

This demo implements a small, production-minded MCP server using FastMCP.
It demonstrates tools, resources, prompts, lifespan management, structured
outputs, and context-aware logging/progress reporting.
"""
from __future__ import annotations

import asyncio
import logging
import os
import sys
from contextlib import asynccontextmanager
from dataclasses import dataclass
from typing import List

from pydantic import BaseModel, Field

from mcp.server.fastmcp import FastMCP, Context
from mcp.server.session import ServerSession
from mcp.server.fastmcp.prompts import base as prompts_base

# Configure simple stderr logging so stdout is reserved for stdio transport
logging.basicConfig(stream=sys.stderr, level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("mcp-demo")


class WeatherData(BaseModel):
    temperature: float = Field(description="Temperature in Celsius")
    condition: str
    humidity: float


class MockDatabase:
    """A tiny async DB mock for demo purposes."""

    def __init__(self) -> None:
        self._connected = False

    async def connect(self) -> None:
        await asyncio.sleep(0.01)
        self._connected = True
        logger.debug("MockDatabase connected")

    async def disconnect(self) -> None:
        await asyncio.sleep(0.01)
        self._connected = False
        logger.debug("MockDatabase disconnected")

    async def query(self, sql: str) -> str:
        await asyncio.sleep(0.01)
        return f"result-of:{sql}"


@dataclass
class AppContext:
    db: MockDatabase


@asynccontextmanager
async def app_lifespan(server: FastMCP):
    db = MockDatabase()
    await db.connect()
    try:
        yield AppContext(db=db)
    finally:
        await db.disconnect()


# Create MCP server instance. The `lifespan` wires up shared resources.
mcp = FastMCP("AutoGPT MCP Demo", lifespan=app_lifespan)


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two integers.

    Returns the integer sum. Validates inputs and raises on invalid types.
    """
    try:
        return int(a) + int(b)
    except Exception as exc:  # broad except for input validation
        logger.exception("add: invalid inputs")
        raise


@mcp.tool()
def get_weather(city: str) -> WeatherData:
    """Return deterministic example weather data for `city`.

    This returns a `WeatherData` model which becomes structured output.
    """
    if not city:
        raise ValueError("city must be a non-empty string")
    # deterministic demo: simple mapping
    mapping = {
        "seattle": (12.3, "rainy", 82.0),
        "santa_monica": (21.0, "sunny", 60.0),
    }
    k = city.replace(" ", "_").lower()
    temp, cond, hum = mapping.get(k, (20.0, "partly-cloudy", 50.0))
    return WeatherData(temperature=temp, condition=cond, humidity=hum)


@mcp.resource("users://{user_id}")
def get_user_profile(user_id: str) -> str:
    """Dynamic resource: return a compact user profile string."""
    # In a real server this would query a DB or external service.
    return f"User:{user_id} (mock-profile)"


@mcp.tool()
async def process_data(data: str, ctx: Context[ServerSession, None]) -> str:
    """Async tool showing context logging and progress reporting.

    - Logs informational messages to the MCP context (Inspector UI).
    - Reports progress twice and returns the processed payload.
    """
    await ctx.info("Starting data processing")
    await ctx.report_progress(0.0, 1.0, "starting")
    await asyncio.sleep(0.01)
    # pretend we do work
    processed = data.strip().upper()
    await ctx.report_progress(0.75, 1.0, "nearly-done")
    await asyncio.sleep(0.01)
    await ctx.info("Processing complete")
    return processed


@mcp.prompt(title="Code Review")
def code_review_prompt(code: str) -> List[prompts_base.Message]:
    """Create a minimal message sequence for code review prompts."""
    return [
        prompts_base.UserMessage("Please review the following code:"),
        prompts_base.UserMessage(code),
        prompts_base.AssistantMessage("I'll review the code and provide feedback."),
    ]


@mcp.tool()
def query_db(sql: str, ctx: Context) -> str:
    """Synchronous wrapper showing access to lifespan context (DB).

    NOTE: This tool demonstrates accessing `ctx.request_context.lifespan_context`.
    """
    try:
        app_ctx: AppContext = ctx.request_context.lifespan_context
        # This demo uses a synchronous wrapper to call the async mock via asyncio.run
        result = asyncio.get_event_loop().run_until_complete(app_ctx.db.query(sql))
        return result
    except Exception:
        logger.exception("query_db failed")
        raise


if __name__ == "__main__":
    transport = os.getenv("MCP_TRANSPORT", "stdio")
    if transport == "streamable-http":
        host = os.getenv("MCP_HOST", "0.0.0.0")
        port = int(os.getenv("MCP_PORT", "8800"))
        stateless = os.getenv("MCP_STATELESS", "false").lower() in ("1", "true", "yes")
        # Run as HTTP server with JSON responses by default for modern clients
        mcp.run(transport="streamable-http", host=host, port=port, stateless_http=stateless, json_response=True)
    else:
        # default: stdio
        mcp.run()
