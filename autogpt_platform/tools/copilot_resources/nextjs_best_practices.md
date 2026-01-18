Source: <https://raw.githubusercontent.com/github/awesome-copilot/main/instructions/nextjs.instructions.md>

# Next.js Best Practices

## 1. Project Structure & Organization

- Use the `app/` directory (App Router) for new projects. Prefer it over legacy `pages/`.
- Top-level folders: `app/`, `public/`, `lib/`, `components/`, `contexts/`, `styles/`, `hooks/`, `types/`.
- Colocation: Place files near use sites; avoid deep nesting.
- Route Groups: Use parentheses for grouping without affecting URL path.

## 2. Server and Client Component Integration (App Router)

- Never use `next/dynamic` with `{ ssr: false }` inside a Server Component.
- Move client-only UI into Client Components (`'use client'`) and import in Server Components.
- Next.js 16+ request APIs are async; await `cookies()`, `headers()`, etc.

## 3. Component Best Practices

- Server Components for data fetching and heavy logic; Client Components for interactivity.
- Use `PascalCase` for components, `camelCase` for hooks, `kebab-case` for assets.
- Prefer TypeScript with `strict` mode; co-locate tests with components.

## 4. API Routes

- Place routes in `app/api/` exporting async functions named by verbs: `GET`, `POST`.
- Validate and sanitize input; use `zod`/`yup` for schema validation.

## 5. Caching & Revalidation

- Prefer Cache Components and use `use cache`, `cacheTag`, `cacheLife`, `revalidateTag` appropriately.

## 6. Tooling

- Turbopack is default dev bundler; configure via `next.config.*`.
- Typed routes supported; follow latest docs.

## 7. Testing, Accessibility, Security, Performance

- Use Jest/RTL/Playwright; enable strict TypeScript; sanitize inputs; optimize Server Components; use Image/Font optimization; follow accessibility best practices.

---

This file condenses actionable Next.js guidance: app-router patterns, server/client boundaries, caching, routing, TypeScript, and modern tooling.
