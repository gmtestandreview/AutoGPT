# Write Tests Prompt

You are an expert in testing React/TypeScript applications. When writing tests for the AutoGPT platform:

## Testing Strategy

- Use React Testing Library for component testing
- Use Playwright for E2E testing
- Write tests that focus on user behavior, not implementation
- Follow the testing pyramid: unit > integration > e2e

## Component Testing Guidelines

- Test component rendering and user interactions
- Mock external dependencies and API calls
- Test accessibility features (screen reader compatibility)
- Verify error states and loading states
- Test keyboard navigation and focus management

## Backend Testing Guidelines

- Use pytest with async support
- Test API endpoints with proper authentication
- Test database operations with transactions
- Mock external services and dependencies
- Test error handling and edge cases

## Testing Checklist

- [ ] Test happy path scenarios
- [ ] Test error states and edge cases
- [ ] Test loading states and async behavior
- [ ] Test user interactions (clicks, form inputs)
- [ ] Test accessibility features
- [ ] Test responsive behavior (mobile/desktop)
- [ ] Mock API calls and external dependencies
- [ ] Verify proper cleanup (memory leaks prevention)

## Frontend Test Patterns

```typescript
import { render, screen, fireEvent } from '@testing-library/react';
import { ComponentName } from './ComponentName';

describe('ComponentName', () => {
  it('should render with proper accessibility attributes', () => {
    render(<ComponentName title="Test" />);
    expect(screen.getByRole('button')).toBeInTheDocument();
  });

  it('should handle user interactions correctly', async () => {
    const onClickMock = jest.fn();
    render(<ComponentName onClick={onClickMock} />);
    
    await fireEvent.click(screen.getByRole('button'));
    expect(onClickMock).toHaveBeenCalledTimes(1);
  });
});
```

## Backend Test Patterns

```python
import pytest
from backend.blocks import BlockName

@pytest.mark.asyncio
async def test_block_execution():
    """Test block executes correctly with valid input."""
    block = BlockName()
    result = await block.run({"input": "test_data"})
    assert result["output"] == "expected_output"

@pytest.mark.asyncio
async def test_block_error_handling():
    """Test block handles errors gracefully."""
    block = BlockName()
    with pytest.raises(ValueError):
        await block.run({"invalid": "input"})
```

## E2E Test Patterns

```typescript
import { test, expect } from '@playwright/test';

test('user can complete authentication flow', async ({ page }) => {
  await page.goto('/login');
  
  await page.fill('[data-testid="email-input"]', 'user@example.com');
  await page.fill('[data-testid="password-input"]', 'password123');
  await page.click('[data-testid="login-button"]');
  
  await expect(page).toHaveURL('/dashboard');
});
```

## AutoGPT-Specific Guidelines

- Test agent block functionality with proper input/output validation
- Test graph execution flow with multiple blocks
- Test real-time updates and WebSocket connections
- Test file upload and processing workflows
- Mock external API integrations (OpenAI, etc.)

## Commands for Running Tests

- Frontend: `pnpm test` or `pnpm test-ui`
- Backend: `poetry run test` or `poetry run pytest path/to/test.py`
- Specific tests: Add `-xvs` flags for detailed output

Always consider:

- Performance implications of tests
- Test data setup and cleanup
- Cross-browser compatibility (for E2E)
- Mobile responsiveness testing
- Security testing (XSS, CSRF protection)
