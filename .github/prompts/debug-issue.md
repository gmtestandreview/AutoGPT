# Debug Issue Prompt

You are an expert debugger for the AutoGPT platform. When debugging issues, follow a systematic approach:

## Debugging Process

### 1. Issue Analysis

- **Reproduce the Issue**: Create minimal steps to reproduce the problem
- **Gather Context**: Collect error messages, logs, and system state
- **Define Scope**: Determine if it's frontend, backend, database, or integration issue
- **Check Recent Changes**: Review recent commits that might have introduced the issue

### 2. Information Gathering

- **Error Messages**: Collect complete stack traces and error details
- **Browser Console**: Check for JavaScript errors and network failures
- **Server Logs**: Review application logs, database logs, and system logs
- **Network Traffic**: Inspect API calls, response codes, and payloads
- **Environment**: Check environment variables, configuration, and dependencies

### 3. Hypothesis Formation

- **Identify Possible Causes**: List potential root causes based on symptoms
- **Prioritize Hypotheses**: Start with most likely causes
- **Create Test Cases**: Design experiments to validate/invalidate hypotheses
- **Document Assumptions**: Keep track of what you're testing and why

### 4. Systematic Investigation

- **Binary Search**: Narrow down the problem area systematically
- **Isolation**: Test components in isolation to identify the faulty component
- **Comparison**: Compare working vs. non-working scenarios
- **Rollback Testing**: Test previous working versions to identify when issue started

## Common Debug Scenarios

### Frontend Debugging

#### React Component Issues

```typescript
// Debug Component Rendering Issues
import { useEffect, useRef } from 'react';

function DebugComponent({ data }: { data: any }) {
  const renderCount = useRef(0);
  
  useEffect(() => {
    renderCount.current++;
    console.log('Component rendered:', renderCount.current, { data });
  });
  
  useEffect(() => {
    console.log('Data changed:', data);
  }, [data]);
  
  // Add debugging breakpoints and logging
  return (
    <div>
      <div>Render count: {renderCount.current}</div>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}
```

#### Network Request Debugging

```typescript
// Debug API Calls
async function debugApiCall(endpoint: string, options: RequestInit) {
  console.group(`API Call: ${endpoint}`);
  console.log('Request options:', options);
  
  try {
    const response = await fetch(endpoint, options);
    console.log('Response status:', response.status);
    console.log('Response headers:', Object.fromEntries(response.headers));
    
    const data = await response.json();
    console.log('Response data:', data);
    
    if (!response.ok) {
      console.error('API Error:', data);
    }
    
    return data;
  } catch (error) {
    console.error('Network Error:', error);
    throw error;
  } finally {
    console.groupEnd();
  }
}
```

### Backend Debugging

#### Python Debugging Techniques

```python
import logging
import traceback
from functools import wraps

# Debug Decorator for Function Tracing
def debug_trace(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        logger = logging.getLogger(func.__module__)
        logger.debug(f"Entering {func.__name__} with args={args}, kwargs={kwargs}")
        
        try:
            result = await func(*args, **kwargs)
            logger.debug(f"Exiting {func.__name__} with result={result}")
            return result
        except Exception as e:
            logger.error(f"Error in {func.__name__}: {str(e)}")
            logger.error(f"Traceback: {traceback.format_exc()}")
            raise
    
    return wrapper

# Database Query Debugging
async def debug_query(query: str, params: dict = None):
    """Debug database queries with timing and parameter logging."""
    import time
    
    start_time = time.time()
    logger.info(f"Executing query: {query}")
    if params:
        logger.info(f"Query parameters: {params}")
    
    try:
        result = await execute_query(query, params)
        execution_time = time.time() - start_time
        logger.info(f"Query completed in {execution_time:.3f}s, rows affected: {len(result) if result else 0}")
        return result
    except Exception as e:
        logger.error(f"Query failed after {time.time() - start_time:.3f}s: {str(e)}")
        raise
```

### Database Debugging

#### SQL Query Analysis

```sql
-- Debug slow queries
EXPLAIN ANALYZE SELECT 
    a.id, a.name, COUNT(r.id) as run_count
FROM agents a
LEFT JOIN agent_runs r ON a.id = r.agent_id
WHERE a.user_id = $1
GROUP BY a.id, a.name
ORDER BY run_count DESC;

-- Check for missing indexes
SELECT 
    schemaname,
    tablename,
    attname,
    n_distinct,
    correlation
FROM pg_stats
WHERE schemaname = 'public'
    AND n_distinct > 100
    AND correlation < 0.1;
```

#### Connection Pool Debugging

```python
import asyncpg
import logging

async def debug_database_pool():
    """Debug database connection pool issues."""
    pool = await asyncpg.create_pool(
        database_url,
        min_size=5,
        max_size=20,
        command_timeout=60
    )
    
    # Monitor pool usage
    logging.info(f"Pool size: {pool.get_size()}")
    logging.info(f"Pool idle connections: {pool.get_idle_size()}")
    
    async with pool.acquire() as conn:
        # Debug connection state
        logging.info(f"Connection status: {conn.is_closed()}")
        result = await conn.fetchval("SELECT 1")
        logging.info(f"Test query result: {result}")
```

## AutoGPT-Specific Debugging

### Agent Execution Debugging

```python
async def debug_agent_execution(agent_id: str, input_data: dict):
    """Debug agent execution flow."""
    logger = logging.getLogger("agent_debug")
    
    # Log execution start
    logger.info(f"Starting agent {agent_id} with input: {input_data}")
    
    # Debug graph validation
    graph = await get_agent_graph(agent_id)
    logger.info(f"Agent graph has {len(graph.nodes)} nodes, {len(graph.edges)} edges")
    
    # Trace block execution
    for node in graph.nodes:
        logger.info(f"Executing block {node.id} ({node.block_type})")
        
        try:
            result = await execute_block(node, input_data)
            logger.info(f"Block {node.id} completed: {result}")
        except Exception as e:
            logger.error(f"Block {node.id} failed: {str(e)}")
            logger.error(f"Block input: {input_data}")
            raise
```

### WebSocket Debugging

```typescript
// Debug WebSocket connections
class DebugWebSocket {
  private ws: WebSocket;
  
  constructor(url: string) {
    console.log(`Connecting to WebSocket: ${url}`);
    this.ws = new WebSocket(url);
    
    this.ws.onopen = (event) => {
      console.log('WebSocket connected:', event);
    };
    
    this.ws.onmessage = (event) => {
      console.log('WebSocket message received:', event.data);
      try {
        const data = JSON.parse(event.data);
        console.log('Parsed message:', data);
      } catch (e) {
        console.log('Raw message (not JSON):', event.data);
      }
    };
    
    this.ws.onerror = (error) => {
      console.error('WebSocket error:', error);
    };
    
    this.ws.onclose = (event) => {
      console.log('WebSocket closed:', event.code, event.reason);
    };
  }
}
```

## Debugging Tools and Techniques

### Browser DevTools

- **Console**: Use console.log, console.group, console.table for structured logging
- **Network Tab**: Monitor API requests, response times, and failure rates
- **Performance Tab**: Profile component renders and identify performance bottlenecks
- **Sources Tab**: Set breakpoints and step through code execution
- **Application Tab**: Inspect localStorage, sessionStorage, and service workers

### Backend Debugging Tools

- **Logging**: Use structured logging with appropriate log levels
- **Debugger**: Use pdb or IDE debugger for interactive debugging
- **Profiling**: Use cProfile or py-spy for performance profiling
- **Database Tools**: Use pgAdmin or similar for SQL debugging
- **Monitoring**: Use APM tools like Sentry or DataDog for production debugging

### Testing for Debugging

```python
# Create minimal reproduction tests
async def test_reproduce_bug():
    """Minimal test to reproduce the reported bug."""
    # Set up minimal conditions
    user = await create_test_user()
    agent = await create_test_agent(user.id)
    
    # Execute the failing scenario
    with pytest.raises(ExpectedError):
        result = await execute_agent(agent.id, {"test": "data"})
    
    # Verify the error condition
    assert "expected error message" in str(result)
```

## Debugging Checklist

### Initial Assessment

- [ ] Can you reproduce the issue consistently?
- [ ] Do you have complete error messages and stack traces?
- [ ] Have you checked recent code changes?
- [ ] Is this affecting all users or specific conditions?
- [ ] Are there any related issues in logs or monitoring?

### Investigation

- [ ] Have you isolated the problem to a specific component?
- [ ] Have you tested with minimal reproduction case?
- [ ] Have you checked environment and configuration?
- [ ] Have you verified network connectivity and external services?
- [ ] Have you tested with different user roles/permissions?

### Resolution

- [ ] Does the fix address the root cause?
- [ ] Have you added tests to prevent regression?
- [ ] Have you verified the fix doesn't break other functionality?
- [ ] Have you updated documentation if needed?
- [ ] Is the fix ready for production deployment?

## Common Issues and Solutions

### Performance Issues

- Use React DevTools Profiler to identify unnecessary re-renders
- Check database query performance with EXPLAIN ANALYZE
- Monitor memory usage for potential leaks
- Profile API response times and optimize slow endpoints

### Authentication Issues

- Verify JWT token validity and expiration
- Check user permissions and role assignments
- Validate OAuth flow and callback handling
- Test with different authentication providers

### Data Inconsistency Issues

- Check database constraints and foreign keys
- Verify transaction handling and rollback logic
- Test concurrent operations and race conditions
- Validate data migration and schema changes

Remember: Good debugging is systematic, methodical, and well-documented. Always verify your assumptions and test your solutions thoroughly.
