# Next.js Development Standards

<!-- Based on: https://github.com/github/awesome-copilot/main/instructions/nextjs.instructions.md -->

This file contains comprehensive Next.js development standards for AutoGPT frontend development.

## Project Structure & Organization

- **Use the `app/` directory** (App Router) for all new projects over legacy `pages/`
- **Top-level folders:**
  - `app/` — Routing, layouts, pages, and route handlers
  - `public/` — Static assets (images, fonts, etc.)
  - `lib/` — Shared utilities, API clients, and logic
  - `components/` — Reusable UI components
  - `hooks/` — Custom React hooks
  - `types/` — TypeScript type definitions
- **Colocation:** Place files near where they're used, avoid deeply nested structures
- **Route Groups:** Use parentheses (e.g., `(admin)`) to group routes without affecting URL
- **Private Folders:** Prefix with `_` to opt out of routing

## Server and Client Component Integration

- **Never use `next/dynamic` with `{ ssr: false }` inside Server Components**
- **Move client-only logic** into dedicated Client Components with `'use client'`
- **Import Client Components directly** in Server Components (no dynamic imports needed)
- **Default to Server Components** unless you need interactivity, state, or browser APIs

## Component Best Practices

- **Server Components (default):** For data fetching, heavy logic, non-interactive UI
- **Client Components:** Add `'use client'` for interactivity, state, or browser APIs
- **Naming Conventions:**
  - `PascalCase` for component files and exports
  - `camelCase` for hooks
  - `kebab-case` for static assets
- **Component Location:**
  - Shared components in `components/`
  - Route-specific components inside relevant route folder

## API Routes (Route Handlers)

- **Location:** Place in `app/api/` (e.g., `app/api/users/route.ts`)
- **HTTP Methods:** Export async functions named after HTTP verbs (`GET`, `POST`, etc.)
- **Request/Response:** Use Web `Request`/`Response` APIs or `NextRequest`/`NextResponse`
- **Validation:** Always validate and sanitize input with libraries like `zod` or `yup`
- **Authentication:** Protect sensitive routes using middleware or server-side checks
- **Avoid calling your own Route Handlers** from Server Components; extract shared logic

## Caching & Revalidation (Next.js 16+)

- **Prefer Cache Components** for memoization/caching in App Router
- **Use `use cache` directive** to opt components/functions into caching
- **Cache tagging:** Use `cacheTag(...)` to associate cached results with tags
- **Revalidation:** Prefer `revalidateTag(tag, 'max')` (stale-while-revalidate)
- **Server Actions:** Use `updateTag(...)` for immediate consistency

## General Best Practices

- **TypeScript:** Use strict mode in `tsconfig.json`
- **ESLint & Prettier:** Use official Next.js ESLint config
- **Environment Variables:**
  - Store secrets in `.env.local`
  - `NEXT_PUBLIC_` variables are inlined at build time
  - Never commit secrets to version control
- **Performance:**
  - Use built-in Image and Font optimization
  - Prefer Cache Components over legacy caching
  - Use Suspense and loading states for async data
  - Keep client bundles small; use Server Components for heavy logic
- **Security:**
  - Sanitize all user input
  - Use HTTPS in production
  - Set secure HTTP headers
  - Prefer server-side authorization

## AutoGPT-Specific Patterns

- **Use generated API hooks** from `@/app/api/__generated__/endpoints/`
- **Follow component architecture** established in `src/components/`
- **Use Tailwind CSS** for styling with design system components
- **Implement error boundaries** and proper error handling
- **Use React Query patterns** via generated hooks for server state
- **Follow established routing patterns** in the AutoGPT platform

## Tooling (Next.js 16+)

- **Turbopack is default** dev bundler; configure via `turbopack` field in `next.config.*`
- **Typed routes are stable** via `typedRoutes` (requires TypeScript)

## Avoid Unnecessary Examples

- **Don't create example/demo files** unless specifically requested
- **Keep repository clean** and production-focused by default
- **Focus on maintainable patterns** over one-off examples
## Tooling
- Turbopack is the default dev bundler; configure via `next.config.*`.
- Use typed routes and follow current Next.js documentation.

## Testing, Accessibility, Security, Performance
- Use Jest/RTL/Playwright; sanitize inputs; optimize images/fonts; implement Suspense/loading states and error boundaries.

---

Use this file for Next.js architecture guidance, code reviews, and Copilot prompt generation.
