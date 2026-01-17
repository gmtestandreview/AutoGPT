---
description: 'TypeScript development standards targeting TypeScript 5.x and ES2022'
applyTo: '**/*.ts'
---

# TypeScript Development Standards

<!-- Based on: https://github.com/github/awesome-copilot/main/instructions/typescript-5-es2022.instructions.md -->

## Core Principles

- **Respect existing architecture** and coding standards
- **Prefer readable, explicit solutions** over clever shortcuts
- **Extend current abstractions** before inventing new ones
- **Prioritize maintainability and clarity** with short methods and clean code

## General Guidelines

- **Target TypeScript 5.x / ES2022** and prefer native features over polyfills
- **Use pure ES modules**; never emit `require`, `module.exports`, or CommonJS helpers
- **Rely on project build/lint/test scripts** unless asked otherwise
- **Note design trade-offs** when intent is not obvious

## Project Organization

- **Follow repository folder structure** for new code
- **Use kebab-case filenames** (e.g., `user-session.ts`, `data-service.ts`)
- **Keep tests, types, and helpers** near their implementation when it aids discovery
- **Reuse or extend shared utilities** before adding new ones

## Naming & Style

- **Use PascalCase** for classes, interfaces, enums, and type aliases
- **Use camelCase** for everything else (functions, variables, properties)
- **Skip interface prefixes** like `I`; rely on descriptive names
- **Name for behavior or domain meaning**, not implementation details

## Type System Best Practices

- **Avoid `any`** (implicit or explicit); prefer `unknown` plus narrowing
- **Use discriminated unions** for realtime events and state machines
- **Centralize shared contracts** instead of duplicating shapes
- **Express intent** with TypeScript utility types (`Readonly`, `Partial`, `Record`)

## Async & Error Handling

- **Use `async/await`** for asynchronous operations
- **Wrap awaits in try/catch** with structured errors
- **Guard edge cases early** to avoid deep nesting
- **Send errors through project logging/telemetry** utilities
- **Surface user-facing errors** via repository notification pattern

## Architecture Patterns

- **Follow dependency injection** or composition patterns from the repository
- **Keep modules single-purpose** and maintain clear interfaces
- **Observe existing initialization/disposal sequences** when wiring into lifecycles
- **Keep transport, domain, and presentation layers** decoupled

## Security Practices

- **Validate and sanitize external input** with schema validators or type guards
- **Avoid dynamic code execution** and untrusted template rendering
- **Encode untrusted content** before rendering HTML; use framework escaping
- **Use parameterized queries** to block injection attacks
- **Keep secrets in secure storage** and request least-privilege scopes

## AutoGPT-Specific Patterns

- **Use generated API hooks** from `@/app/api/__generated__/endpoints/`
- **Follow frontend component structure** patterns established in the codebase
- **Implement proper error boundaries** and error handling
- **Use React Query patterns** for server state management
- **Follow Next.js App Router conventions** for routing and data fetching

## Performance Considerations

- **Lazy-load heavy dependencies** and dispose when done
- **Defer expensive work** until users need it
- **Batch or debounce high-frequency events** to reduce thrash
- **Track resource lifetimes** to prevent leaks

## Testing Standards

- **Add or update unit tests** with project framework and naming style
- **Expand integration tests** when behavior crosses modules
- **Run targeted test scripts** for quick feedback
- **Avoid brittle timing assertions**; prefer fake timers or injected clocks

## Documentation

- **Add JSDoc to public APIs** with `@remarks` or `@example` when helpful
- **Write comments that capture intent** and remove stale notes during refactors
- **Update architecture docs** when introducing significant patterns