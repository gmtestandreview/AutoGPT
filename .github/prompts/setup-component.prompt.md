---
title: "Setup React Component"
description: "Create a new React component with proper TypeScript typing, hooks, and testing setup"
category: "Frontend Development"
tags: ["react", "typescript", "components", "frontend"]
version: "1.0.0"
---

# Setup React Component

You are an expert React developer working on the AutoGPT platform. Create a new React component with the following specifications:

## Component Requirements

**Component Name:** {COMPONENT_NAME}
**Purpose:** {COMPONENT_PURPOSE}
**Props Interface:** {COMPONENT_PROPS}

## Implementation Checklist

### 1. Component Structure
- [ ] Create component file with proper naming (`PascalCase.tsx`)
- [ ] Use functional component with TypeScript
- [ ] Define proper props interface
- [ ] Implement proper error boundaries if needed
- [ ] Add proper JSDoc documentation

### 2. TypeScript Integration
- [ ] Define comprehensive props interface
- [ ] Use proper React types (`React.FC`, event handlers)
- [ ] Implement generic types if applicable
- [ ] Export types for external usage

### 3. Hooks & State Management
- [ ] Use appropriate hooks (`useState`, `useEffect`, `useCallback`, etc.)
- [ ] Implement proper dependency arrays
- [ ] Add cleanup functions where needed
- [ ] Use custom hooks for complex logic

### 4. Styling & Design System
- [ ] Use Tailwind CSS classes
- [ ] Follow AutoGPT design system patterns
- [ ] Implement responsive design
- [ ] Add proper accessibility attributes

### 5. Testing Setup
- [ ] Create test file (`Component.test.tsx`)
- [ ] Write unit tests for core functionality
- [ ] Test different prop combinations
- [ ] Add accessibility tests
- [ ] Create Storybook story if applicable

### 6. Performance Considerations
- [ ] Use `React.memo` if appropriate
- [ ] Implement proper `useMemo`/`useCallback` usage
- [ ] Consider code splitting for large components
- [ ] Optimize re-renders

## Code Template

```typescript
import React from 'react';

interface {COMPONENT_NAME}Props {
  // Define your props here
}

/**
 * {COMPONENT_PURPOSE}
 */
export function {COMPONENT_NAME}({
  // destructure props
}: {COMPONENT_NAME}Props): JSX.Element {
  // Component implementation
  
  return (
    <div>
      {/* Component JSX */}
    </div>
  );
}

export default {COMPONENT_NAME};
```

## AutoGPT-Specific Guidelines

- **Use generated API hooks** from `@/app/api/__generated__/endpoints/`
- **Follow component structure** in `src/components/`
- **Use Phosphor Icons** for consistency
- **Implement proper error handling** with `<ErrorCard />` component
- **Use design tokens** instead of hardcoded values
- **Follow established patterns** in existing components

## Validation Steps

1. **Functionality:** Component renders correctly with all prop combinations
2. **TypeScript:** No type errors, proper intellisense
3. **Accessibility:** Screen reader compatible, keyboard navigation
4. **Performance:** No unnecessary re-renders
5. **Testing:** All tests pass, good coverage
6. **Integration:** Works properly in AutoGPT context

Please implement the component following these guidelines and ensure it integrates seamlessly with the AutoGPT platform architecture.