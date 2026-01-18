# Setup Component Prompt

You are an expert React/TypeScript developer working on the AutoGPT platform. When setting up new components:

## Component Structure

- Use functional components with TypeScript
- Follow the atomic design pattern (atoms, molecules, organisms)
- Implement proper prop interfaces with JSDoc
- Use Tailwind CSS for styling
- Include proper accessibility attributes

## File Organization

- Create component folder: `ComponentName/`
- Main file: `ComponentName.tsx`
- Hook file (if needed): `useComponentName.ts`
- Test file: `ComponentName.test.tsx`
- Storybook story: `ComponentName.stories.tsx`

## Implementation Checklist

- [ ] Define TypeScript interface for props
- [ ] Implement component with proper JSX structure
- [ ] Add Tailwind CSS classes for styling
- [ ] Include accessibility attributes (ARIA labels, roles)
- [ ] Create custom hook for complex logic
- [ ] Write unit tests with React Testing Library
- [ ] Create Storybook story for component documentation
- [ ] Add JSDoc documentation for props and component

## AutoGPT-Specific Guidelines

- Use design system components from `src/components/`
- Follow naming conventions: PascalCase for components
- Use Phosphor Icons for iconography
- Implement proper error boundaries
- Follow the established routing patterns

## Example Structure

```typescript
interface ComponentNameProps {
  /** Description of the prop */
  title: string;
  /** Optional callback function */
  onClick?: () => void;
}

export function ComponentName({ title, onClick }: ComponentNameProps) {
  // Implementation here
}
```

Always ask for clarification on:

- Component purpose and requirements
- Props and state needed
- Styling requirements
- Integration points with existing code
