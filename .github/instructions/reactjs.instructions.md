# ReactJS Development Standards

<!-- Based on: https://github.com/github/awesome-copilot/main/instructions/reactjs.instructions.md -->

This file contains comprehensive ReactJS development standards for AutoGPT.

## Project Context

- **Latest React (19+)** with TypeScript for type safety
- **Functional components with hooks** as default pattern
- **Follow React's official style guide** and best practices
- **Use modern build tools** (Vite, Next.js, or custom setup)
- **Component composition** and reusability patterns

## Architecture & Patterns

- **Use functional components with hooks** as the primary pattern
- **Implement component composition** over inheritance
- **Organize by feature or domain** for scalability
- **Separate presentational and container** components clearly
- **Use custom hooks** for reusable stateful logic
- **Clear component hierarchies** with proper data flow

## TypeScript Integration

- **Use TypeScript interfaces** for props, state, and component definitions
- **Define proper types** for event handlers and refs
- **Implement generic components** where appropriate
- **Use strict mode** in `tsconfig.json` for type safety
- **Leverage React's built-in types** (`React.FC`, `React.ComponentProps`, etc.)
- **Create union types** for component variants and states

## Component Design

- **Single responsibility principle** for components
- **Descriptive and consistent** naming conventions
- **Proper prop validation** with TypeScript or PropTypes
- **Testable and reusable** design patterns
- **Small, focused components** with single concerns
- **Composition patterns** (render props, children as functions)

## State Management

- **Use `useState`** for local component state
- **Use `useReducer`** for complex state logic
- **Use `useContext`** for sharing state across component trees
- **External state management** (Redux Toolkit, Zustand) for complex apps
- **Proper state normalization** and data structures
- **React Query or SWR** for server state management

## Hooks & Effects

- **Use `useEffect`** with proper dependency arrays to avoid infinite loops
- **Implement cleanup functions** in effects to prevent memory leaks
- **Use `useMemo` and `useCallback`** for performance optimization when needed
- **Create custom hooks** for reusable stateful logic
- **Follow rules of hooks** (only call at top level)
- **Use `useRef`** for DOM elements and storing mutable values

## Performance Optimization

- **Use `React.memo`** for component memoization when appropriate
- **Code splitting** with `React.lazy` and `Suspense`
- **Bundle optimization** with tree shaking and dynamic imports
- **Judicious use** of `useMemo` and `useCallback` to prevent unnecessary re-renders
- **Virtual scrolling** for large lists
- **Profile with React DevTools** to identify bottlenecks

## AutoGPT-Specific Patterns

- **Use generated API hooks** for data fetching
- **Follow established component structure** in `src/components/`
- **Use Tailwind CSS** with design system components
- **Implement proper error boundaries** and error handling
- **Use React Query patterns** for server state
- **Follow Next.js patterns** for routing and navigation

## Styling
- Use CSS Modules, Styled Components, or CSS-in-JS.
- Mobile-first responsive design; accessibility with ARIA attributes.

## Performance
- Use `React.memo`, code-splitting, virtualized lists for large data.
- Profile with React DevTools.

## Data Fetching
- Use React Query or SWR; implement loading/error states and optimistic updates.

## Testing
- Use React Testing Library and Jest; focus on behavior, co-locate tests.

## Security & Accessibility
- Sanitize user inputs to prevent XSS; HTTPS for externals; implement ARIA roles; test with screen readers.

---

Apply this file for code reviews, component design, and Copilot generation prompts for React components.
