# AutoGPT MCP Server Demo

This folder contains a small, self-contained Model Context Protocol (MCP) server demo implemented in Python using `mcp.server.fastmcp.FastMCP`.

Quick start

1. Install dependencies (recommended in a venv):

```bash
pip install -r requirements.txt
```

2. Run as stdio server (default):

```bash
python server.py
```

3. Run as HTTP server:

```bash
MCP_TRANSPORT=streamable-http MCP_HOST=127.0.0.1 MCP_PORT=8800 python server.py
```

What it demonstrates

- Declarative tools with `@mcp.tool()`
- Structured outputs using Pydantic models
- Dynamic resources with `@mcp.resource()`
- Prompts with `@mcp.prompt()` returning message sequences
- Lifespan-managed shared resources (mock DB)
- Context-aware logging, `ctx.info()`, and `ctx.report_progress()`

Notes

- This demo uses a `MockDatabase` for portability; replace with a real DB in production and implement proper error handling and retries.
- For packaging, see `pyproject.toml`.
