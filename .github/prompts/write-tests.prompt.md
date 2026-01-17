---
title: "Write Comprehensive Tests"
description: "Create thorough test suite for components, functions, or API endpoints"
category: "Testing"
tags: ["testing", "jest", "playwright", "pytest", "quality-assurance"]
version: "1.0.0"
---

# Write Comprehensive Tests

You are a testing expert working on the AutoGPT platform. Create a comprehensive test suite for the specified code component.

## Test Target

**Component/Function:** {TEST_TARGET}
**Type:** {TEST_TYPE} (unit/integration/e2e)
**Testing Framework:** {FRAMEWORK} (Jest/Playwright/pytest)

## Testing Strategy

### 1. Test Planning
- [ ] Identify all public methods/functions to test
- [ ] Define test scenarios (happy path, edge cases, error conditions)
- [ ] Determine test data requirements
- [ ] Plan mock/stub strategy for dependencies

### 2. Test Categories

#### Unit Tests
- [ ] **Function behavior** - Test all public methods
- [ ] **Input validation** - Test with various input types
- [ ] **Edge cases** - Empty inputs, null/undefined, boundary values
- [ ] **Error handling** - Exception scenarios and error messages
- [ ] **State changes** - Verify state transitions (for components)

#### Integration Tests
- [ ] **API interactions** - Test API calls and responses
- [ ] **Database operations** - Test CRUD operations
- [ ] **Service integration** - Test service dependencies
- [ ] **Component integration** - Test component interactions

#### End-to-End Tests
- [ ] **User workflows** - Complete user journeys
- [ ] **Cross-browser testing** - Multiple browser compatibility
- [ ] **Mobile responsiveness** - Touch and mobile interactions
- [ ] **Performance** - Load times and responsiveness

### 3. AutoGPT-Specific Testing

#### Backend (Python/FastAPI)
```python
import pytest
from fastapi.testclient import TestClient
from unittest.mock import Mock, patch

# Test API endpoint
def test_{endpoint_name}_success():
    # Arrange
    client = TestClient(app)
    
    # Act
    response = client.get("/api/endpoint")
    
    # Assert
    assert response.status_code == 200
    assert response.json()["data"] is not None

# Test with user authentication
def test_{endpoint_name}_requires_auth():
    client = TestClient(app)
    response = client.get("/api/protected-endpoint")
    assert response.status_code == 401

# Test database operations
@pytest.mark.asyncio
async def test_database_operation():
    # Use test database
    async with test_db_session() as session:
        # Test CRUD operations
        pass
```

#### Frontend (React/TypeScript)
```typescript
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import userEvent from '@testing-library/user-event';
import { ComponentName } from './ComponentName';

describe('ComponentName', () => {
  const renderComponent = (props = {}) => {
    const queryClient = new QueryClient({
      defaultOptions: { queries: { retry: false } }
    });
    
    return render(
      <QueryClientProvider client={queryClient}>
        <ComponentName {...props} />
      </QueryClientProvider>
    );
  };

  it('renders correctly with default props', () => {
    renderComponent();
    expect(screen.getByRole('button')).toBeInTheDocument();
  });

  it('handles user interaction', async () => {
    const user = userEvent.setup();
    const onClickMock = jest.fn();
    
    renderComponent({ onClick: onClickMock });
    
    await user.click(screen.getByRole('button'));
    
    expect(onClickMock).toHaveBeenCalledTimes(1);
  });
});
```

#### E2E Tests (Playwright)
```typescript
import { test, expect } from '@playwright/test';

test.describe('Agent Management', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/agents');
  });

  test('creates new agent successfully', async ({ page }) => {
    // Navigate to create agent
    await page.click('[data-testid="create-agent-button"]');
    
    // Fill form
    await page.fill('[data-testid="agent-name-input"]', 'Test Agent');
    await page.fill('[data-testid="agent-description"]', 'Test Description');
    
    // Submit
    await page.click('[data-testid="submit-button"]');
    
    // Verify creation
    await expect(page.locator('[data-testid="agent-card"]')).toBeVisible();
  });

  test('validates required fields', async ({ page }) => {
    await page.click('[data-testid="create-agent-button"]');
    await page.click('[data-testid="submit-button"]');
    
    await expect(page.locator('[data-testid="error-message"]')).toContainText('Name is required');
  });
});
```

## Test Implementation Checklist

### 4. Setup & Configuration
- [ ] Configure test environment variables
- [ ] Set up test database (if applicable)
- [ ] Configure mocks for external services
- [ ] Set up test data factories/fixtures

### 5. Test Coverage
- [ ] Aim for >80% code coverage
- [ ] Cover all conditional branches
- [ ] Test all error paths
- [ ] Include boundary condition tests

### 6. Test Quality
- [ ] **Descriptive test names** - Clear what is being tested
- [ ] **AAA Pattern** - Arrange, Act, Assert structure
- [ ] **Independent tests** - Each test can run in isolation
- [ ] **Deterministic** - Tests produce consistent results
- [ ] **Fast execution** - Tests run quickly

### 7. Mocking Strategy
- [ ] Mock external API calls
- [ ] Mock database connections (for unit tests)
- [ ] Stub time-dependent functions
- [ ] Mock file system operations
- [ ] Use test doubles appropriately

### 8. Data Management
- [ ] Use test-specific data
- [ ] Clean up after tests
- [ ] Isolate test data between tests
- [ ] Use factories for complex objects

## AutoGPT Test Patterns

### Backend Testing
- **Use pytest fixtures** for database setup
- **Mock Prisma operations** for unit tests
- **Test user authorization** for protected endpoints
- **Validate input schemas** with Pydantic
- **Test async operations** properly

### Frontend Testing
- **Use React Testing Library** best practices
- **Mock API hooks** from generated endpoints
- **Test component interactions** with user events
- **Validate accessibility** with screen readers
- **Test error boundaries** and error states

### Integration Testing
- **Test full API workflows** with real database
- **Validate frontend-backend integration**
- **Test authentication flows**
- **Verify data persistence**

## Execution Commands

```bash
# Backend tests
poetry run pytest path/to/test.py -v
poetry run pytest --cov=backend --cov-report=html

# Frontend tests  
pnpm test
pnpm test:coverage

# E2E tests
pnpm test:e2e
pnpm test:e2e --headed
```

## Success Criteria

1. **All tests pass** consistently
2. **Good coverage** (>80% for critical paths)
3. **Fast execution** (<5 minutes for full suite)
4. **Clear failure messages** for debugging
5. **No flaky tests** - consistent results
6. **Maintainable** - easy to update with code changes

Implement comprehensive tests that ensure code quality, catch regressions, and provide confidence in the AutoGPT platform's reliability.