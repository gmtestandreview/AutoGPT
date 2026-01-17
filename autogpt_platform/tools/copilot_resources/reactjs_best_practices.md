Source: https://raw.githubusercontent.com/github/awesome-copilot/main/instructions/reactjs.instructions.md

# ReactJS Development Standards

## Project Context
- Latest React (19+). Use TypeScript for type safety. Functional components with hooks as default.
- Follow React official style guide. Use modern build tools (Vite, CRA, or Webpack).

## Architecture
- Functional components and hooks. Component composition over inheritance.
- Organize by feature/domain; separate presentational and container components.
- Use custom hooks for reusable stateful logic.

## TypeScript Integration
- Use TypeScript interfaces for props; enable `strict` mode.
- Use `React.FC` and built-in types; define generic components where appropriate.

## Hooks and Effects
- Proper dependency arrays; cleanup in effects to avoid leaks.
- Use `useMemo`/`useCallback` judiciously.

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

This file summarizes recommended React patterns: hooks, TypeScript, component composition, performance, testing, and accessibility.
