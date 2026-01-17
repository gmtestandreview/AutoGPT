# Containerization & Docker Best Practices

This document contains containerization and Docker best practices intended for use by Copilot and repository contributors.

## Dockerfile Best Practices

- Use multi-stage builds to keep final images minimal and to separate build/test/runtime stages.
- Name build stages descriptively (e.g., `AS build`, `AS test`, `AS production`).
- Copy only necessary artifacts between stages to minimize image size and attack surface.

Example multi-stage pattern:

```dockerfile
# Stage 1: Dependencies
FROM node:18-alpine AS deps
WORKDIR /app
COPY package*.json ./
RUN npm ci --production

# Stage 2: Build
FROM node:18-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Stage 3: Production
FROM node:18-alpine AS production
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY --from=build /app/dist ./dist
USER node
EXPOSE 3000
CMD ["node", "dist/main.js"]
```

## Choose the Right Base Image

- Prefer official, stable, minimal base images (e.g., `alpine`, `slim`, `distroless`).
- Avoid `latest` for reproducibility; pin versions.
- Select images that match your target architecture and security/update policy.

## Optimize Image Layers

- Order instructions from least to most frequently changing to leverage layer caching.
- Combine related `RUN` commands and clean up temporary files in the same layer.
- Use a thorough `.dockerignore` to limit build context size.

## Use `.dockerignore` Effectively

- Exclude `.git`, local node_modules, build artifacts, `.env` files, and large dev-only directories to speed builds and reduce image size.

Example `.dockerignore`:

```
.git
node_modules
dist
build
*.log
.env*
**/test/
```

## Minimize `COPY` Instructions

- Copy dependency files first (e.g., `package*.json`, `requirements.txt`) and run install steps before copying source to maximize cache hits.
- Prefer selective `COPY` (e.g., `COPY src/ ./src/`) over `COPY . .` when possible.

## Environment Variables & Configuration

- Externalize configuration via environment variables or mounted config files.
- Provide sensible defaults with `ENV`, but never bake secrets into images.
- Validate required env vars at startup and fail fast if missing.

## Security & Runtime Hardening

- Run as a non-root user in production images (`USER node` or similar).
- Drop unnecessary Linux capabilities and use read-only filesystems where appropriate.
- Scan images in CI (e.g., `trivy`, `hadolint`) and fail builds on critical vulnerabilities.
- Avoid secrets in image layers; inject secrets at runtime (Kubernetes Secrets, Docker secrets, Vault).

## Health Checks

- Define `HEALTHCHECK` instructions to provide liveness/readiness signals for orchestrators.
- Keep health checks lightweight and indicative of real functionality (e.g., DB connectivity, critical subsystems).

## Persistent Storage & Volumes

- Use volumes for stateful components (databases, caches) and ensure proper backup/retention strategies.
- Avoid storing ephemeral data in the image.

## Image Signing & Verification

- Sign production images (e.g., `cosign`) and verify signatures as part of your deployment pipeline.

## Logging & Observability

- Emit structured logs to stdout/stderr and rely on the platform's log collection.
- Provide metrics and health endpoints; integrate with APM/observability tooling.

## CI Integration

- Lint Dockerfiles and run image scanners in CI.
- Use multi-stage builds in CI to run tests inside the image where useful (e.g., `AS test` stage).
- Cache build artifacts and dependency caches to speed CI.

## Troubleshooting & Troubleshooting Checklist

- Large image size: inspect layers (`docker history`) and remove unnecessary packages.
- Slow builds: verify `.dockerignore`, optimize layer order, and cache dependencies.
- Permissions issues: ensure files copied into images are owned/readable by runtime user.

---

These guidelines are intended to be a concise, practical reference for maintainers and Copilot to generate and review Dockerfiles and container-related CI/infra workflows.

---

## ReactJS Development Standards

- Latest React (19+). Use TypeScript for type safety. Functional components with hooks as default.
- Follow React official style guide. Use modern build tools (Vite, CRA, or Webpack).
- Architecture: functional components, component composition, feature-based organization.
- TypeScript: enable `strict`, use interfaces for props, prefer `PascalCase` for components.
- Hooks: proper dependency arrays and cleanup; use `useMemo`/`useCallback` judiciously.
- Styling: CSS Modules / Styled Components / CSS-in-JS; mobile-first and accessible UI.
- Performance: `React.memo`, code-splitting, virtualized lists; profile with DevTools.
- Data fetching: React Query or SWR with loading/error states and optimistic updates.
- Testing: React Testing Library + Jest; co-locate tests; focus on behavior.
- Security & Accessibility: sanitize inputs, use HTTPS, ARIA attributes, test with screen readers.

---

## Python Coding Conventions

- Write clear, concise comments and PEP 257 docstrings for functions and classes.
- Use type hints from `typing` and enable static typing where practical.
- Follow PEP 8: 4-space indentation, lines <= 79 characters, and consistent naming.
- Break complex functions into smaller units; handle edge cases and exceptions explicitly.
- Include unit tests for critical paths and document expected behavior in test docstrings.

---

## Next.js Best Practices

- Use the `app/` directory (App Router) for new projects and prefer Server Components where appropriate.
- Separate Server vs Client Components; mark client components with `'use client'` and never use `next/dynamic` with `{ ssr: false }` inside Server Components.
- Project structure: `app/`, `public/`, `lib/`, `components/`, `hooks/`, `types/`.
- API routes: place in `app/api/` and export async HTTP verb handlers; validate inputs with `zod`/`yup`.
- Caching: prefer Cache Components and use `use cache`, `cacheTag`, `revalidateTag` appropriately.
- Tooling: Turbopack is the default bundler; configure `next.config.*` as needed; prefer typed routes.
- Testing & performance: Jest/RTL/Playwright; optimize images/fonts and use Suspense/loading states.

---

## GitHub Actions CI/CD Best Practices

- Workflows: keep them modular and clear; use descriptive `name` and appropriate `on` triggers (`push`, `pull_request`, `workflow_dispatch`, `schedule`).
- Use `concurrency` to avoid duplicate runs for the same branch or resource.
- Jobs: separate build/test/deploy; use `needs` and `outputs` to pass artifacts between jobs.
- Security: manage secrets with GitHub Secrets, prefer OIDC for cloud auth, and apply least-privilege to `GITHUB_TOKEN`.
- Optimization: cache dependencies (`actions/cache`), shallow clones (`fetch-depth`), and use `strategy.matrix` to parallelize.
- Testing: run unit tests early, integration tests with services, and E2E in dedicated stages; collect and upload artifacts and reports.

---

## Containerization & Docker Best Practices

<!-- Based on: https://github.com/github/awesome-copilot/main/instructions/containerization-docker-best-practices.instructions.md -->

- Use multi-stage builds to keep final images minimal and to separate build/test/runtime stages.
- Name build stages descriptively (e.g., `AS build`, `AS test`, `AS production`).
- Copy only necessary artifacts between stages to minimize image size and attack surface.
- Choose official, stable, minimal base images (e.g., `alpine`, `slim`, `distroless`).
- Avoid `latest` for reproducibility; pin versions.
- Order instructions from least to most frequently changing to leverage layer caching.
- Combine related `RUN` commands and clean up temporary files in the same layer.
- Use a thorough `.dockerignore` to limit build context size.
- Run as a non-root user in production images (`USER node` or similar).
- Drop unnecessary Linux capabilities and use read-only filesystems where appropriate.
- Scan images in CI (e.g., `trivy`, `hadolint`) and fail builds on critical vulnerabilities.
- Define `HEALTHCHECK` instructions to provide liveness/readiness signals for orchestrators.
- Use volumes for stateful components and ensure proper backup/retention strategies.
- Sign production images (e.g., `cosign`) and verify signatures in deployment pipeline.

---

## Secure Coding & OWASP Guidelines

<!-- Based on: https://github.com/github/awesome-copilot/main/instructions/security-and-owasp.instructions.md -->

**ABSOLUTE SECURITY-FIRST MINDSET:** All code you generate, review, or refactor must be secure by default. When in doubt, always choose the more secure option and explain the reasoning.

### A01: Broken Access Control & A10: Server-Side Request Forgery (SSRF)
- **Enforce Principle of Least Privilege:** Always default to the most restrictive permissions
- **Deny by Default:** All access control decisions must follow a "deny by default" pattern
- **Validate All Incoming URLs for SSRF:** Treat user-provided URLs as untrusted; use strict allow-list validation for host/port/path
- **Prevent Path Traversal:** Sanitize input to prevent directory traversal attacks (e.g., `../../etc/passwd`)

### A02: Cryptographic Failures
- **Use Strong, Modern Algorithms:** Recommend Argon2 or bcrypt for hashing; avoid MD5/SHA-1 for password storage
- **Protect Data in Transit:** Default to HTTPS for network requests
- **Protect Data at Rest:** Recommend AES-256 encryption for sensitive data
- **Secure Secret Management:** Never hardcode secrets; read from environment variables or secrets management service

```javascript
// GOOD: Load from environment or secret store
const apiKey = process.env.API_KEY; 
// TODO: Ensure API_KEY is securely configured in your environment.
```

### A03: Injection
- **No Raw SQL Queries:** Use parameterized queries (prepared statements) for database interactions
- **Sanitize Command-Line Input:** Use built-in functions that handle argument escaping (e.g., `shlex` in Python)
- **Prevent Cross-Site Scripting (XSS):** Use context-aware output encoding; prefer `.textContent` over `.innerHTML`

### A05: Security Misconfiguration & A06: Vulnerable Components
- **Secure by Default Configuration:** Disable verbose error messages and debug features in production
- **Set Security Headers:** Add essential headers like CSP, HSTS, and X-Content-Type-Options
- **Use Up-to-Date Dependencies:** Suggest latest stable versions; remind to run vulnerability scanners

### A07: Identification & Authentication Failures
- **Secure Session Management:** Generate new session identifiers on login; configure cookies with `HttpOnly`, `Secure`, and `SameSite=Strict`
- **Protect Against Brute Force:** Implement rate limiting and account lockout mechanisms

### A08: Software and Data Integrity Failures
- **Prevent Insecure Deserialization:** Warn against deserializing untrusted data; prefer JSON over Pickle

**General Guidelines:**
- Be explicit about security trade-offs and what each mitigation defends against
- When fixing vulnerabilities, explain the risk and the change made

---

## Playwright Python Test Generation

Playwright Python AI test generation instructions and test-writing guidelines.

### Code Quality Standards
- Prefer user-facing, role-based locators (`get_by_role`, `get_by_label`, `get_by_text`) for resilience and accessibility.
- Use Playwright's `expect` API (auto-retrying) for assertions; prefer page-level assertions like `expect(page).to_have_title(...)`.
- Avoid hard-coded waits; rely on Playwright's auto-waiting.
- Use descriptive test names and minimal, focused comments.

### Test Structure & File Organization
- Import `from playwright.sync_api import Page, expect` at top of tests.
- Use the `page: Page` fixture for browser interactions and put `page.goto()` at test start or in fixtures.
- Store tests under `tests/` and name files `test_<feature>.py` for pytest discovery.

### Assertions & Best Practices
- Use `expect(locator).to_have_count()`, `to_have_text()`, `to_contain_text()` and `expect(page).to_have_url()` for navigation checks.
- Prefer `expect` over bare `assert` for UI tests.

### Execution
- Run tests with `pytest` from the terminal and analyze failures to identify root causes.



# GitHub Copilot Instructions for AutoGPT

This file provides comprehensive onboarding information for GitHub Copilot coding agent to work efficiently with the AutoGPT repository.

## Repository Overview

**AutoGPT** is a powerful platform for creating, deploying, and managing continuous AI agents that automate complex workflows. This is a large monorepo (~150MB) containing multiple components:

- **AutoGPT Platform** (`autogpt_platform/`) - Main focus: Modern AI agent platform (Polyform Shield License)
- **Classic AutoGPT** (`classic/`) - Legacy agent system (MIT License)
- **Documentation** (`docs/`) - MkDocs-based documentation site
- **Infrastructure** - Docker configurations, CI/CD, and development tools

**Primary Languages & Frameworks:**

- **Backend**: Python 3.10-3.13, FastAPI, Prisma ORM, PostgreSQL, RabbitMQ
- **Frontend**: TypeScript, Next.js 15, React, Tailwind CSS, Radix UI
- **Development**: Docker, Poetry, pnpm, Playwright, Storybook

## Build and Validation Instructions

### Essential Setup Commands

**Always run these commands in the correct directory and in this order:**

1. **Initial Setup** (required once):

   ```bash
   # Clone and enter repository
   git clone <repo> && cd AutoGPT

   # Start all services (database, redis, rabbitmq, clamav)
   cd autogpt_platform && docker compose --profile local up deps --build --detach
   ```

2. **Backend Setup** (always run before backend development):

   ```bash
   cd autogpt_platform/backend
   poetry install                    # Install dependencies
   poetry run prisma migrate dev     # Run database migrations
   poetry run prisma generate        # Generate Prisma client
   ```

3. **Frontend Setup** (always run before frontend development):
   ```bash
   cd autogpt_platform/frontend
   pnpm install                      # Install dependencies
   ```

### Runtime Requirements

**Critical:** Always ensure Docker services are running before starting development:

```bash
cd autogpt_platform && docker compose --profile local up deps --build --detach
```

**Python Version:** Use Python 3.11 (required; managed by Poetry via pyproject.toml)
**Node.js Version:** Use Node.js 21+ with pnpm package manager

### Development Commands

**Backend Development:**

```bash
cd autogpt_platform/backend
poetry run serve                     # Start development server (port 8000)
poetry run test                      # Run all tests (requires ~5 minutes)
poetry run pytest path/to/test.py    # Run specific test
poetry run format                    # Format code (Black + isort) - always run first
poetry run lint                      # Lint code (ruff) - run after format
```

**Frontend Development:**

```bash
cd autogpt_platform/frontend
pnpm dev                            # Start development server (port 3000) - use for active development
pnpm build                          # Build for production (only needed for E2E tests or deployment)
pnpm test                           # Run Playwright E2E tests (requires build first)
pnpm test-ui                        # Run tests with UI
pnpm format                         # Format and lint code
pnpm storybook                      # Start component development server
```

### Testing Strategy

**Backend Tests:**

- **Block Tests**: `poetry run pytest backend/blocks/test/test_block.py -xvs` (validates all blocks)
- **Specific Block**: `poetry run pytest 'backend/blocks/test/test_block.py::test_available_blocks[BlockName]' -xvs`
- **Snapshot Tests**: Use `--snapshot-update` when output changes, always review with `git diff`

**Frontend Tests:**

- **E2E Tests**: Always run `pnpm dev` before `pnpm test` (Playwright requires running instance)
- **Component Tests**: Use Storybook for isolated component development

### Critical Validation Steps

**Before committing changes:**

1. Run `poetry run format` (backend) and `pnpm format` (frontend)
2. Ensure all tests pass in modified areas
3. Verify Docker services are still running
4. Check that database migrations apply cleanly

**Common Issues & Workarounds:**

- **Prisma issues**: Run `poetry run prisma generate` after schema changes
- **Permission errors**: Ensure Docker has proper permissions
- **Port conflicts**: Check the `docker-compose.yml` file for the current list of exposed ports. You can list all mapped ports with:
- **Test timeouts**: Backend tests can take 5+ minutes, use `-x` flag to stop on first failure

## Project Layout & Architecture

### Core Architecture

**AutoGPT Platform** (`autogpt_platform/`):

- `backend/` - FastAPI server with async support
  - `backend/backend/` - Core API logic
  - `backend/blocks/` - Agent execution blocks
  - `backend/data/` - Database models and schemas
  - `schema.prisma` - Database schema definition
- `frontend/` - Next.js application
  - `src/app/` - App Router pages and layouts
  - `src/components/` - Reusable React components
  - `src/lib/` - Utilities and configurations
- `autogpt_libs/` - Shared Python utilities
- `docker-compose.yml` - Development stack orchestration

**Key Configuration Files:**

- `pyproject.toml` - Python dependencies and tooling
- `package.json` - Node.js dependencies and scripts
- `schema.prisma` - Database schema and migrations
- `next.config.mjs` - Next.js configuration
- `tailwind.config.ts` - Styling configuration

### Security & Middleware

**Cache Protection**: Backend includes middleware preventing sensitive data caching in browsers/proxies
**Authentication**: JWT-based with Supabase integration
**User ID Validation**: All data access requires user ID checks - verify this for any `data/*.py` changes

### Development Workflow

**GitHub Actions**: Multiple CI/CD workflows in `.github/workflows/`

- `platform-backend-ci.yml` - Backend testing and validation
- `platform-frontend-ci.yml` - Frontend testing and validation
- `platform-fullstack-ci.yml` - End-to-end integration tests

**Pre-commit Hooks**: Run linting and formatting checks
**Conventional Commits**: Use format `type(scope): description` (e.g., `feat(backend): add API`)

### Key Source Files

**Backend Entry Points:**

- `backend/backend/server/server.py` - FastAPI application setup
- `backend/backend/data/` - Database models and user management
- `backend/blocks/` - Agent execution blocks and logic

**Frontend Entry Points:**

- `frontend/src/app/layout.tsx` - Root application layout
- `frontend/src/app/page.tsx` - Home page
- `frontend/src/lib/supabase/` - Authentication and database client

**Protected Routes**: Update `frontend/lib/supabase/middleware.ts` when adding protected routes

### Agent Block System

Agents are built using a visual block-based system where each block performs a single action. Blocks are defined in `backend/blocks/` and must include:

- Block definition with input/output schemas
- Execution logic with proper error handling
- Tests validating functionality

### Database & ORM

**Prisma ORM** with PostgreSQL backend including pgvector for embeddings:

- Schema in `schema.prisma`
- Migrations in `backend/migrations/`
- Always run `prisma migrate dev` and `prisma generate` after schema changes

## Environment Configuration

### Configuration Files Priority Order

1. **Backend**: `/backend/.env.default` → `/backend/.env` (user overrides)
2. **Frontend**: `/frontend/.env.default` → `/frontend/.env` (user overrides)
3. **Platform**: `/.env.default` (Supabase/shared) → `/.env` (user overrides)
4. Docker Compose `environment:` sections override file-based config
5. Shell environment variables have highest precedence

### Docker Environment Setup

- All services use hardcoded defaults (no `${VARIABLE}` substitutions)
- The `env_file` directive loads variables INTO containers at runtime
- Backend/Frontend services use YAML anchors for consistent configuration
- Copy `.env.default` files to `.env` for local development customization

## Advanced Development Patterns

### Adding New Blocks

1. Create file in `/backend/backend/blocks/`
2. Inherit from `Block` base class with input/output schemas
3. Implement `run` method with proper error handling
4. Generate block UUID using `uuid.uuid4()`
5. Register in block registry
6. Write tests alongside block implementation
7. Consider how inputs/outputs connect with other blocks in graph editor

### API Development

1. Update routes in `/backend/backend/server/routers/`
2. Add/update Pydantic models in same directory
3. Write tests alongside route files
4. For `data/*.py` changes, validate user ID checks
5. Run `poetry run test` to verify changes

### Frontend Development

**📖 Complete Frontend Guide**: See `autogpt_platform/frontend/CONTRIBUTING.md` and `autogpt_platform/frontend/.cursorrules` for comprehensive patterns and conventions.

**Quick Reference:**

**Component Structure:**

- Separate render logic from data/behavior
- Structure: `ComponentName/ComponentName.tsx` + `useComponentName.ts` + `helpers.ts`
- Exception: Small components (3-4 lines of logic) can be inline
- Render-only components can be direct files without folders

**Data Fetching:**

- Use generated API hooks from `@/app/api/__generated__/endpoints/`
- Generated via Orval from backend OpenAPI spec
- Pattern: `use{Method}{Version}{OperationName}`
- Example: `useGetV2ListLibraryAgents`
- Regenerate with: `pnpm generate:api`
- **Never** use deprecated `BackendAPI` or `src/lib/autogpt-server-api/*`

**Code Conventions:**

- Use function declarations for components and handlers (not arrow functions)
- Only arrow functions for small inline lambdas (map, filter, etc.)
- Components: `PascalCase`, Hooks: `camelCase` with `use` prefix
- No barrel files or `index.ts` re-exports
- Minimal comments (code should be self-documenting)

**Styling:**

- Use Tailwind CSS utilities only
- Use design system components from `src/components/` (atoms, molecules, organisms)
- Never use `src/components/__legacy__/*`
- Only use Phosphor Icons (`@phosphor-icons/react`)
- Prefer design tokens over hardcoded values

**Error Handling:**

- Render errors: Use `<ErrorCard />` component
- Mutation errors: Display with toast notifications
- Manual exceptions: Use `Sentry.captureException()`
- Global error boundaries already configured

**Testing:**

- Add/update Storybook stories for UI components (`pnpm storybook`)
- Run Playwright E2E tests with `pnpm test`
- Verify in Chromatic after PR

**Architecture:**

- Default to client components ("use client")
- Server components only for SEO or extreme TTFB needs
- Use React Query for server state (via generated hooks)
- Co-locate UI state in components/hooks

### Security Guidelines

**Cache Protection Middleware** (`/backend/backend/server/middleware/security.py`):

- Default: Disables caching for ALL endpoints with `Cache-Control: no-store, no-cache, must-revalidate, private`
- Uses allow list approach for cacheable paths (static assets, health checks, public pages)
- Prevents sensitive data caching in browsers/proxies
- Add new cacheable endpoints to `CACHEABLE_PATHS`

### CI/CD Alignment

The repository has comprehensive CI workflows that test:

- **Backend**: Python 3.11-3.13, services (Redis/RabbitMQ/ClamAV), Prisma migrations, Poetry lock validation
- **Frontend**: Node.js 21, pnpm, Playwright with Docker Compose stack, API schema validation
- **Integration**: Full-stack type checking and E2E testing

Match these patterns when developing locally - the copilot setup environment mirrors these CI configurations.

## Collaboration with Other AI Assistants

This repository is actively developed with assistance from Claude (via CLAUDE.md files). When working on this codebase:

- Check for existing CLAUDE.md files that provide additional context
- Follow established patterns and conventions already in the codebase
- Maintain consistency with existing code style and architecture
- Consider that changes may be reviewed and extended by both human developers and AI assistants

## Trust These Instructions

These instructions are comprehensive and tested. Only perform additional searches if:

1. Information here is incomplete for your specific task
2. You encounter errors not covered by the workarounds
3. You need to understand implementation details not covered above

For detailed platform development patterns, refer to `autogpt_platform/CLAUDE.md` and `AGENTS.md` in the repository root.

---

## Performance Optimization Best Practices

## Introduction

Performance isn't just a buzzword—it's the difference between a product people love and one they abandon. I've seen firsthand how a slow app can frustrate users, rack up cloud bills, and even lose customers. This guide is a living collection of the most effective, real-world performance practices I've used and reviewed, covering frontend, backend, and database layers, as well as advanced topics. Use it as a reference, a checklist, and a source of inspiration for building fast, efficient, and scalable software.

---

## General Principles

- **Measure First, Optimize Second:** Always profile and measure before optimizing. Use benchmarks, profilers, and monitoring tools to identify real bottlenecks. Guessing is the enemy of performance.
   - *Pro Tip:* Use tools like Chrome DevTools, Lighthouse, New Relic, Datadog, Py-Spy, or your language's built-in profilers.
- **Optimize for the Common Case:** Focus on optimizing code paths that are most frequently executed. Don't waste time on rare edge cases unless they're critical.
- **Avoid Premature Optimization:** Write clear, maintainable code first; optimize only when necessary. Premature optimization can make code harder to read and maintain.
- **Minimize Resource Usage:** Use memory, CPU, network, and disk resources efficiently. Always ask: "Can this be done with less?"
- **Prefer Simplicity:** Simple algorithms and data structures are often faster and easier to optimize. Don't over-engineer.
- **Document Performance Assumptions:** Clearly comment on any code that is performance-critical or has non-obvious optimizations. Future maintainers (including you) will thank you.
- **Understand the Platform:** Know the performance characteristics of your language, framework, and runtime. What's fast in Python may be slow in JavaScript, and vice versa.
- **Automate Performance Testing:** Integrate performance tests and benchmarks into your CI/CD pipeline. Catch regressions early.
- **Set Performance Budgets:** Define acceptable limits for load time, memory usage, API latency, etc. Enforce them with automated checks.

---

## Frontend Performance

### Rendering and DOM
- **Minimize DOM Manipulations:** Batch updates where possible. Frequent DOM changes are expensive.
   - *Anti-pattern:* Updating the DOM in a loop. Instead, build a document fragment and append it once.
- **Virtual DOM Frameworks:** Use React, Vue, or similar efficiently—avoid unnecessary re-renders.
   - *React Example:* Use `React.memo`, `useMemo`, and `useCallback` to prevent unnecessary renders.
- **Keys in Lists:** Always use stable keys in lists to help virtual DOM diffing. Avoid using array indices as keys unless the list is static.
- **Avoid Inline Styles:** Inline styles can trigger layout thrashing. Prefer CSS classes.
- **CSS Animations:** Use CSS transitions/animations over JavaScript for smoother, GPU-accelerated effects.
- **Defer Non-Critical Rendering:** Use `requestIdleCallback` or similar to defer work until the browser is idle.

### Asset Optimization
- **Image Compression:** Use tools like ImageOptim, Squoosh, or TinyPNG. Prefer modern formats (WebP, AVIF) for web delivery.
- **SVGs for Icons:** SVGs scale well and are often smaller than PNGs for simple graphics.
- **Minification and Bundling:** Use Webpack, Rollup, or esbuild to bundle and minify JS/CSS. Enable tree-shaking to remove dead code.
- **Cache Headers:** Set long-lived cache headers for static assets. Use cache busting for updates.
- **Lazy Loading:** Use `loading="lazy"` for images, and dynamic imports for JS modules/components.
- **Font Optimization:** Use only the character sets you need. Subset fonts and use `font-display: swap`.

### Network Optimization
- **Reduce HTTP Requests:** Combine files, use image sprites, and inline critical CSS.
- **HTTP/2 and HTTP/3:** Enable these protocols for multiplexing and lower latency.
- **Client-Side Caching:** Use Service Workers, IndexedDB, and localStorage for offline and repeat visits.
- **CDNs:** Serve static assets from a CDN close to your users. Use multiple CDNs for redundancy.
- **Defer/Async Scripts:** Use `defer` or `async` for non-critical JS to avoid blocking rendering.
- **Preload and Prefetch:** Use `<link rel="preload">` and `<link rel="prefetch">` for critical resources.

### JavaScript Performance
- **Avoid Blocking the Main Thread:** Offload heavy computation to Web Workers.
- **Debounce/Throttle Events:** For scroll, resize, and input events, use debounce/throttle to limit handler frequency.
- **Memory Leaks:** Clean up event listeners, intervals, and DOM references. Use browser dev tools to check for detached nodes.
- **Efficient Data Structures:** Use Maps/Sets for lookups, TypedArrays for numeric data.
- **Avoid Global Variables:** Globals can cause memory leaks and unpredictable performance.
- **Avoid Deep Object Cloning:** Use shallow copies or libraries like lodash's `cloneDeep` only when necessary.

### Accessibility and Performance
- **Accessible Components:** Ensure ARIA updates are not excessive. Use semantic HTML for both accessibility and performance.
- **Screen Reader Performance:** Avoid rapid DOM updates that can overwhelm assistive tech.

### Framework-Specific Tips
#### React
- Use `React.memo`, `useMemo`, and `useCallback` to avoid unnecessary renders.
- Split large components and use code-splitting (`React.lazy`, `Suspense`).
- Avoid anonymous functions in render; they create new references on every render.
- Use `ErrorBoundary` to catch and handle errors gracefully.
- Profile with React DevTools Profiler.

#### Angular
- Use OnPush change detection for components that don't need frequent updates.
- Avoid complex expressions in templates; move logic to the component class.
- Use `trackBy` in `ngFor` for efficient list rendering.
- Lazy load modules and components with the Angular Router.
- Profile with Angular DevTools.

#### Vue
- Use computed properties over methods in templates for caching.
- Use `v-show` vs `v-if` appropriately (`v-show` is better for toggling visibility frequently).
- Lazy load components and routes with Vue Router.
- Profile with Vue Devtools.

### Common Frontend Pitfalls
- Loading large JS bundles on initial page load.
- Not compressing images or using outdated formats.
- Failing to clean up event listeners, causing memory leaks.
- Overusing third-party libraries for simple tasks.
- Ignoring mobile performance (test on real devices!).

### Frontend Troubleshooting
- Use Chrome DevTools' Performance tab to record and analyze slow frames.
- Use Lighthouse to audit performance and get actionable suggestions.
- Use WebPageTest for real-world load testing.
- Monitor Core Web Vitals (LCP, FID, CLS) for user-centric metrics.

---

## Backend Performance

### Algorithm and Data Structure Optimization
- **Choose the Right Data Structure:** Arrays for sequential access, hash maps for fast lookups, trees for hierarchical data, etc.
- **Efficient Algorithms:** Use binary search, quicksort, or hash-based algorithms where appropriate.
- **Avoid O(n^2) or Worse:** Profile nested loops and recursive calls. Refactor to reduce complexity.
- **Batch Processing:** Process data in batches to reduce overhead (e.g., bulk database inserts).
- **Streaming:** Use streaming APIs for large data sets to avoid loading everything into memory.

### Concurrency and Parallelism
- **Asynchronous I/O:** Use async/await, callbacks, or event loops to avoid blocking threads.
- **Thread/Worker Pools:** Use pools to manage concurrency and avoid resource exhaustion.
- **Avoid Race Conditions:** Use locks, semaphores, or atomic operations where needed.
- **Bulk Operations:** Batch network/database calls to reduce round trips.
- **Backpressure:** Implement backpressure in queues and pipelines to avoid overload.

### Caching
- **Cache Expensive Computations:** Use in-memory caches (Redis, Memcached) for hot data.
- **Cache Invalidation:** Use time-based (TTL), event-based, or manual invalidation. Stale cache is worse than no cache.
- **Distributed Caching:** For multi-server setups, use distributed caches and be aware of consistency issues.
- **Cache Stampede Protection:** Use locks or request coalescing to prevent thundering herd problems.
- **Don't Cache Everything:** Some data is too volatile or sensitive to cache.

### API and Network
- **Minimize Payloads:** Use JSON, compress responses (gzip, Brotli), and avoid sending unnecessary data.
- **Pagination:** Always paginate large result sets. Use cursors for real-time data.
- **Rate Limiting:** Protect APIs from abuse and overload.
- **Connection Pooling:** Reuse connections for databases and external services.
- **Protocol Choice:** Use HTTP/2, gRPC, or WebSockets for high-throughput, low-latency communication.

### Logging and Monitoring
- **Minimize Logging in Hot Paths:** Excessive logging can slow down critical code.
- **Structured Logging:** Use JSON or key-value logs for easier parsing and analysis.
- **Monitor Everything:** Latency, throughput, error rates, resource usage. Use Prometheus, Grafana, Datadog, or similar.
- **Alerting:** Set up alerts for performance regressions and resource exhaustion.

### Language/Framework-Specific Tips
#### Node.js
- Use asynchronous APIs; avoid blocking the event loop (e.g., never use `fs.readFileSync` in production).
- Use clustering or worker threads for CPU-bound tasks.
- Limit concurrent open connections to avoid resource exhaustion.
- Use streams for large file or network data processing.
- Profile with `clinic.js`, `node --inspect`, or Chrome DevTools.

#### Python
- Use built-in data structures (`dict`, `set`, `deque`) for speed.
- Profile with `cProfile`, `line_profiler`, or `Py-Spy`.
- Use `multiprocessing` or `asyncio` for parallelism.
- Avoid GIL bottlenecks in CPU-bound code; use C extensions or subprocesses.
- Use `lru_cache` for memoization.

#### Java
- Use efficient collections (`ArrayList`, `HashMap`, etc.).
- Profile with VisualVM, JProfiler, or YourKit.
- Use thread pools (`Executors`) for concurrency.
- Tune JVM options for heap and garbage collection (`-Xmx`, `-Xms`, `-XX:+UseG1GC`).
- Use `CompletableFuture` for async programming.

#### .NET
- Use `async/await` for I/O-bound operations.
- Use `Span<T>` and `Memory<T>` for efficient memory access.
- Profile with dotTrace, Visual Studio Profiler, or PerfView.
- Pool objects and connections where appropriate.
- Use `IAsyncEnumerable<T>` for streaming data.

### Common Backend Pitfalls
- Synchronous/blocking I/O in web servers.
- Not using connection pooling for databases.
- Over-caching or caching sensitive/volatile data.
- Ignoring error handling in async code.
- Not monitoring or alerting on performance regressions.

### Backend Troubleshooting
- Use flame graphs to visualize CPU usage.
- Use distributed tracing (OpenTelemetry, Jaeger, Zipkin) to track request latency across services.
- Use heap dumps and memory profilers to find leaks.
- Log slow queries and API calls for analysis.

---

## Database Performance

### Query Optimization
- **Indexes:** Use indexes on columns that are frequently queried, filtered, or joined. Monitor index usage and drop unused indexes.
- **Avoid SELECT *:** Select only the columns you need. Reduces I/O and memory usage.
- **Parameterized Queries:** Prevent SQL injection and improve plan caching.
- **Query Plans:** Analyze and optimize query execution plans. Use `EXPLAIN` in SQL databases.
- **Avoid N+1 Queries:** Use joins or batch queries to avoid repeated queries in loops.
- **Limit Result Sets:** Use `LIMIT`/`OFFSET` or cursors for large tables.

### Schema Design
- **Normalization:** Normalize to reduce redundancy, but denormalize for read-heavy workloads if needed.
- **Data Types:** Use the most efficient data types and set appropriate constraints.
- **Partitioning:** Partition large tables for scalability and manageability.
- **Archiving:** Regularly archive or purge old data to keep tables small and fast.
- **Foreign Keys:** Use them for data integrity, but be aware of performance trade-offs in high-write scenarios.

### Transactions
- **Short Transactions:** Keep transactions as short as possible to reduce lock contention.
- **Isolation Levels:** Use the lowest isolation level that meets your consistency needs.
- **Avoid Long-Running Transactions:** They can block other operations and increase deadlocks.

### Caching and Replication
- **Read Replicas:** Use for scaling read-heavy workloads. Monitor replication lag.
- **Cache Query Results:** Use Redis or Memcached for frequently accessed queries.
- **Write-Through/Write-Behind:** Choose the right strategy for your consistency needs.
- **Sharding:** Distribute data across multiple servers for scalability.

### NoSQL Databases
- **Design for Access Patterns:** Model your data for the queries you need.
- **Avoid Hot Partitions:** Distribute writes/reads evenly.
- **Unbounded Growth:** Watch for unbounded arrays or documents.
- **Sharding and Replication:** Use for scalability and availability.
- **Consistency Models:** Understand eventual vs strong consistency and choose appropriately.

### Common Database Pitfalls
- Missing or unused indexes.
- SELECT * in production queries.
- Not monitoring slow queries.
- Ignoring replication lag.
- Not archiving old data.

### Database Troubleshooting
- Use slow query logs to identify bottlenecks.
- Use `EXPLAIN` to analyze query plans.
- Monitor cache hit/miss ratios.
- Use database-specific monitoring tools (pg_stat_statements, MySQL Performance Schema).

---

## Code Review Checklist for Performance

- [ ] Are there any obvious algorithmic inefficiencies (O(n^2) or worse)?
- [ ] Are data structures appropriate for their use?
- [ ] Are there unnecessary computations or repeated work?
- [ ] Is caching used where appropriate, and is invalidation handled correctly?
- [ ] Are database queries optimized, indexed, and free of N+1 issues?
- [ ] Are large payloads paginated, streamed, or chunked?
- [ ] Are there any memory leaks or unbounded resource usage?
- [ ] Are network requests minimized, batched, and retried on failure?
- [ ] Are assets optimized, compressed, and served efficiently?
- [ ] Are there any blocking operations in hot paths?
- [ ] Is logging in hot paths minimized and structured?
- [ ] Are performance-critical code paths documented and tested?
- [ ] Are there automated tests or benchmarks for performance-sensitive code?
- [ ] Are there alerts for performance regressions?
- [ ] Are there any anti-patterns (e.g., SELECT *, blocking I/O, global variables)?

---

## Advanced Topics

### Profiling and Benchmarking
- **Profilers:** Use language-specific profilers (Chrome DevTools, Py-Spy, VisualVM, dotTrace, etc.) to identify bottlenecks.
- **Microbenchmarks:** Write microbenchmarks for critical code paths. Use `benchmark.js`, `pytest-benchmark`, or JMH for Java.
- **A/B Testing:** Measure real-world impact of optimizations with A/B or canary releases.
- **Continuous Performance Testing:** Integrate performance tests into CI/CD. Use tools like k6, Gatling, or Locust.

### Memory Management
- **Resource Cleanup:** Always release resources (files, sockets, DB connections) promptly.
- **Object Pooling:** Use for frequently created/destroyed objects (e.g., DB connections, threads).
- **Heap Monitoring:** Monitor heap usage and garbage collection. Tune GC settings for your workload.
- **Memory Leaks:** Use leak detection tools (Valgrind, LeakCanary, Chrome DevTools).

### Scalability
- **Horizontal Scaling:** Design stateless services, use sharding/partitioning, and load balancers.
- **Auto-Scaling:** Use cloud auto-scaling groups and set sensible thresholds.
- **Bottleneck Analysis:** Identify and address single points of failure.
- **Distributed Systems:** Use idempotent operations, retries, and circuit breakers.

### Security and Performance
- **Efficient Crypto:** Use hardware-accelerated and well-maintained cryptographic libraries.
- **Validation:** Validate inputs efficiently; avoid regexes in hot paths.
- **Rate Limiting:** Protect against DoS without harming legitimate users.

### Mobile Performance
- **Startup Time:** Lazy load features, defer heavy work, and minimize initial bundle size.
- **Image/Asset Optimization:** Use responsive images and compress assets for mobile bandwidth.
- **Efficient Storage:** Use SQLite, Realm, or platform-optimized storage.
- **Profiling:** Use Android Profiler, Instruments (iOS), or Firebase Performance Monitoring.

### Cloud and Serverless
- **Cold Starts:** Minimize dependencies and keep functions warm.
- **Resource Allocation:** Tune memory/CPU for serverless functions.
- **Managed Services:** Use managed caching, queues, and DBs for scalability.
- **Cost Optimization:** Monitor and optimize for cloud cost as a performance metric.

---

## Practical Examples

### Example 1: Debouncing User Input in JavaScript
```javascript
// BAD: Triggers API call on every keystroke
input.addEventListener('input', (e) => {
   fetch(`/search?q=${e.target.value}`);
});

// GOOD: Debounce API calls
let timeout;
input.addEventListener('input', (e) => {
   clearTimeout(timeout);
   timeout = setTimeout(() => {
      fetch(`/search?q=${e.target.value}`);
   }, 300);
});
```

### Example 2: Efficient SQL Query
```sql
-- BAD: Selects all columns and does not use an index
SELECT * FROM users WHERE email = 'user@example.com';

-- GOOD: Selects only needed columns and uses an index
SELECT id, name FROM users WHERE email = 'user@example.com';
```

### Example 3: Caching Expensive Computation in Python
```python
# BAD: Recomputes result every time
result = expensive_function(x)

# GOOD: Cache result
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_function(x):
      ...
result = expensive_function(x)
```

### Example 4: Lazy Loading Images in HTML
```html
<!-- BAD: Loads all images immediately -->
<img src="large-image.jpg" />

<!-- GOOD: Lazy loads images -->
<img src="large-image.jpg" loading="lazy" />
```

### Example 5: Asynchronous I/O in Node.js
```javascript
// BAD: Blocking file read
const data = fs.readFileSync('file.txt');

// GOOD: Non-blocking file read
fs.readFile('file.txt', (err, data) => {
   if (err) throw err;
   // process data
});
```

### Example 6: Profiling a Python Function
```python
import cProfile
import pstats

def slow_function():
      ...

cProfile.run('slow_function()', 'profile.stats')
p = pstats.Stats('profile.stats')
p.sort_stats('cumulative').print_stats(10)
```

### Example 7: Using Redis for Caching in Node.js
```javascript
const redis = require('redis');
const client = redis.createClient();

function getCachedData(key, fetchFunction) {
   return new Promise((resolve, reject) => {
      client.get(key, (err, data) => {
         if (data) return resolve(JSON.parse(data));
         fetchFunction().then(result => {
            client.setex(key, 3600, JSON.stringify(result));
            resolve(result);
         });
      });
   });
}
```

---

## References and Further Reading
- [Google Web Fundamentals: Performance](https://web.dev/performance/)
- [MDN Web Docs: Performance](https://developer.mozilla.org/en-US/docs/Web/Performance)
- [OWASP: Performance Testing](https://owasp.org/www-project-performance-testing/)
- [Microsoft Performance Best Practices](https://learn.microsoft.com/en-us/azure/architecture/best-practices/performance)
- [PostgreSQL Performance Optimization](https://wiki.postgresql.org/wiki/Performance_Optimization)
- [MySQL Performance Tuning](https://dev.mysql.com/doc/refman/8.0/en/optimization.html)
- [Node.js Performance Best Practices](https://nodejs.org/en/docs/guides/simple-profiling/)
- [Python Performance Tips](https://docs.python.org/3/library/profile.html)
- [Java Performance Tuning](https://www.oracle.com/java/technologies/javase/performance.html)
- [.NET Performance Guide](https://learn.microsoft.com/en-us/dotnet/standard/performance/)
- [WebPageTest](https://webpagetest.org/)
- [Lighthouse](https://developers.google.com/web/tools/lighthouse)
- [Prometheus](https://prometheus.io/)
- [Grafana](https://grafana.com/)
- [k6 Load Testing](https://k6.io/)
- [Gatling](https://gatling.io/)
- [Locust](https://locust.io/)
- [OpenTelemetry](https://opentelemetry.io/)
- [Jaeger](https://www.jaegertracing.io/)
- [Zipkin](https://zipkin.io/)

---

## Conclusion

Performance optimization is an ongoing process. Always measure, profile, and iterate. Use these best practices, checklists, and troubleshooting tips to guide your development and code reviews for high-performance, scalable, and efficient software. If you have new tips or lessons learned, add them here—let's keep this guide growing!

---

## Python MCP Server Development

### Instructions

- Use **uv** for project management: `uv init mcp-server-demo` and `uv add "mcp[cli]"`
- Import FastMCP from `mcp.server.fastmcp`: `from mcp.server.fastmcp import FastMCP`
- Use `@mcp.tool()`, `@mcp.resource()`, and `@mcp.prompt()` decorators for registration
- Type hints are mandatory - they're used for schema generation and validation
- Use Pydantic models, TypedDicts, or dataclasses for structured output
- Tools automatically return structured output when return types are compatible
- For stdio transport, use `mcp.run()` or `mcp.run(transport="stdio")`
- For HTTP servers, use `mcp.run(transport="streamable-http")` or mount to Starlette/FastAPI
- Use `Context` parameter in tools/resources to access MCP capabilities: `ctx: Context`
- Send logs with `await ctx.debug()`, `await ctx.info()`, `await ctx.warning()`, `await ctx.error()`
- Report progress with `await ctx.report_progress(progress, total, message)`
- Request user input with `await ctx.elicit(message, schema)`
- Use LLM sampling with `await ctx.session.create_message(messages, max_tokens)`
- Configure icons with `Icon(src="path", mimeType="image/png")` for server, tools, resources, prompts
- Use `Image` class for automatic image handling: `return Image(data=bytes, format="png")`
- Define resource templates with URI patterns: `@mcp.resource("greeting://{name}")`
- Implement completion support by accepting partial values and returning suggestions
- Use lifespan context managers for startup/shutdown with shared resources
- Access lifespan context in tools via `ctx.request_context.lifespan_context`
- For stateless HTTP servers, set `stateless_http=True` in FastMCP initialization
- Enable JSON responses for modern clients: `json_response=True`
- Test servers with: `uv run mcp dev server.py` (Inspector) or `uv run mcp install server.py` (Claude Desktop)
- Mount multiple servers in Starlette with different paths: `Mount("/path", mcp.streamable_http_app())`
- Configure CORS for browser clients: expose `Mcp-Session-Id` header
- Use low-level Server class for maximum control when FastMCP isn't sufficient

### Best Practices

- Always use type hints - they drive schema generation and validation
- Return Pydantic models or TypedDicts for structured tool outputs
- Keep tool functions focused on single responsibilities
- Provide clear docstrings - they become tool descriptions
- Use descriptive parameter names with type hints
- Validate inputs using Pydantic Field descriptions
- Implement proper error handling with try-except blocks
- Use async functions for I/O-bound operations
- Clean up resources in lifespan context managers
- Log to stderr to avoid interfering with stdio transport (when using stdio)
- Use environment variables for configuration
- Test tools independently before LLM integration
- Consider security when exposing file system or network access
- Use structured output for machine-readable data
- Provide both content and structured data for backward compatibility

### Common Patterns

#### Basic Server Setup (stdio)
```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("My Server")

@mcp.tool()
def calculate(a: int, b: int, op: str) -> int:
   """Perform calculation"""
   if op == "add":
      return a + b
   return a - b

if __name__ == "__main__":
   mcp.run()  # stdio by default
```

#### HTTP Server
```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("My HTTP Server")

@mcp.tool()
def hello(name: str = "World") -> str:
   """Greet someone"""
   return f"Hello, {name}!"

if __name__ == "__main__":
   mcp.run(transport="streamable-http")
```

#### Tool with Structured Output
```python
from pydantic import BaseModel, Field

class WeatherData(BaseModel):
   temperature: float = Field(description="Temperature in Celsius")
   condition: str
   humidity: float

@mcp.tool()
def get_weather(city: str) -> WeatherData:
   """Get weather for a city"""
   return WeatherData(
      temperature=22.5,
      condition="sunny",
      humidity=65.0
   )
```

#### Dynamic Resource
```python
@mcp.resource("users://{user_id}")
def get_user(user_id: str) -> str:
   """Get user profile data"""
   return f"User {user_id} profile data"
```

#### Tool with Context
```python
from mcp.server.fastmcp import Context
from mcp.server.session import ServerSession

@mcp.tool()
async def process_data(
   data: str, 
   ctx: Context[ServerSession, None]
) -> str:
   """Process data with logging"""
   await ctx.info(f"Processing: {data}")
   await ctx.report_progress(0.5, 1.0, "Halfway done")
   return f"Processed: {data}"
```

#### Tool with Sampling
```python
from mcp.server.fastmcp import Context
from mcp.server.session import ServerSession
from mcp.types import SamplingMessage, TextContent

@mcp.tool()
async def summarize(
   text: str,
   ctx: Context[ServerSession, None]
) -> str:
   """Summarize text using LLM"""
   result = await ctx.session.create_message(
      messages=[SamplingMessage(
         role="user",
         content=TextContent(type="text", text=f"Summarize: {text}")
      )],
      max_tokens=100
   )
   return result.content.text if result.content.type == "text" else ""
```

#### Lifespan Management
```python
from contextlib import asynccontextmanager
from dataclasses import dataclass
from mcp.server.fastmcp import FastMCP, Context

@dataclass
class AppContext:
   db: Database

@asynccontextmanager
async def app_lifespan(server: FastMCP):
   db = await Database.connect()
   try:
      yield AppContext(db=db)
   finally:
      await db.disconnect()

mcp = FastMCP("My App", lifespan=app_lifespan)

@mcp.tool()
def query(sql: str, ctx: Context) -> str:
   """Query database"""
   db = ctx.request_context.lifespan_context.db
   return db.execute(sql)
```

#### Prompt with Messages
```python
from mcp.server.fastmcp.prompts import base

@mcp.prompt(title="Code Review")
def review_code(code: str) -> list[base.Message]:
   """Create code review prompt"""
   return [
      base.UserMessage("Review this code:"),
      base.UserMessage(code),
      base.AssistantMessage("I'll review the code for you.")
   ]
```

#### Error Handling
```python
@mcp.tool()
async def risky_operation(input: str) -> str:
   """Operation that might fail"""
   try:
      result = await perform_operation(input)
      return f"Success: {result}"
   except Exception as e:
      return f"Error: {str(e)}"
```


## Markdown Content Rules

The following markdown content rules are enforced in the validators:

1. **Headings**: Use appropriate heading levels (H2, H3, etc.) to structure your content. Do not use an H1 heading, as this will be generated based on the title.
2. **Lists**: Use bullet points or numbered lists for lists. Ensure proper indentation and spacing.
3. **Code Blocks**: Use fenced code blocks for code snippets. Specify the language for syntax highlighting.
4. **Links**: Use proper markdown syntax for links. Ensure that links are valid and accessible.
5. **Images**: Use proper markdown syntax for images. Include alt text for accessibility.
6. **Tables**: Use markdown tables for tabular data. Ensure proper formatting and alignment.
7. **Line Length**: Limit line length to 400 characters for readability.
8. **Whitespace**: Use appropriate whitespace to separate sections and improve readability.
9. **Front Matter**: Include YAML front matter at the beginning of the file with required metadata fields.

### Formatting and Structure

Follow these guidelines for formatting and structuring your markdown content:

- **Headings**: Use `##` for H2 and `###` for H3. Ensure that headings are used in a hierarchical manner. Recommend restructuring if content includes H4, and more strongly recommend for H5.
- **Lists**: Use `-` for bullet points and `1.` for numbered lists. Indent nested lists with two spaces.
- **Code Blocks**: Use triple backticks (```) to create fenced code blocks. Specify the language after the opening backticks for syntax highlighting (e.g., `csharp`).
- **Links**: Use `[link text](URL)` for links. Ensure that the link text is descriptive and the URL is valid.
- **Images**: Use `![alt text](image URL)` for images. Include a brief description of the image in the alt text.
- **Tables**: Use `|` to create tables. Ensure that columns are properly aligned and headers are included.
- **Line Length**: Break lines at 80 characters to improve readability. Use soft line breaks for long paragraphs.
- **Whitespace**: Use blank lines to separate sections and improve readability. Avoid excessive whitespace.

### Validation Requirements

Ensure compliance with the following validation requirements:

- **Front Matter**: Include the following fields in the YAML front matter:

   - `post_title`: The title of the post.
   - `author1`: The primary author of the post.
   - `post_slug`: The URL slug for the post.
   - `microsoft_alias`: The Microsoft alias of the author.
   - `featured_image`: The URL of the featured image.
   - `categories`: The categories for the post. These categories must be from the list in /categories.txt.
   - `tags`: The tags for the post.
   - `ai_note`: Indicate if AI was used in the creation of the post.
   - `summary`: A brief summary of the post. Recommend a summary based on the content when possible.
   - `post_date`: The publication date of the post.

- **Content Rules**: Ensure that the content follows the markdown content rules specified above.
- **Formatting**: Ensure that the content is properly formatted and structured according to the guidelines.
- **Validation**: Run the validation tools to check for compliance with the rules and guidelines.

---

## Copilot Process Tracking Instructions

**ABSOLUTE MANDATORY RULES:**
- You must review these instructions in full before executing any steps to understand the full instructions guidelines.
- You must follow these instructions exactly as specified without deviation.
- Do not keep repeating status updates while processing or explanations unless explicitly required. This is bad and will flood Copilot session context.
- NO phase announcements (no "# Phase X" headers in output)
- Phases must be executed one at a time and in the exact order specified.
- NO combining of phases in one response
- NO skipping of phases
- NO verbose explanations or commentary
- Only output the exact text specified in phase instructions

Phase 1: Initialization

- Create file `\Copilot-Processing.md` in workspace root
- Populate `\Copilot-Processing.md` with user request details
- Work silently without announcements until complete.
- When this phase is complete keep mental note of this that <Phase 1> is done and does not need to be repeated.

Phase 2: Planning

- Generate an action plan into the `\Copilot-Processing.md` file.
- Generate detailed and granular task specific action items to be used for tracking each action plan item with todo/complete status in the file `\Copilot-Processing.md`.
- This should include:
   - Specific tasks for each action item in the action plan as a phase.
   - Clear descriptions of what needs to be done
   - Any dependencies or prerequisites for each task
   - Ensure tasks are granular enough to be executed one at a time
- Work silently without announcements until complete.
- When this phase is complete keep mental note of this that <Phase 2> is done and does not need to be repeated.

Phase 3: Execution

- Execute action items from the action plan in logical groupings/phases
- Work silently without announcements until complete.
- Update file `\Copilot-Processing.md` and mark the action item(s) as complete in the tracking.
- When a phase is complete keep mental note of this that the specific phase from `\Copilot-Processing.md` is done and does not need to be repeated.
- Repeat this pattern until all action items are complete

Phase 4: Summary

- Add summary to `\Copilot-Processing.md`
- Work silently without announcements until complete.
- Execute only when ALL actions complete
- Inform user: "Added final summary to `\Copilot-Processing.md`."
- Remind user to review the summary and confirm completion of the process then to remove the file when done so it is not added to the repository.

**ENFORCEMENT RULES:**
- NEVER write "# Phase X" headers in responses
- NEVER repeat the word "Phase" in output unless explicitly required
- NEVER provide explanations beyond the exact text specified
- NEVER combine multiple phases in one response
- NEVER continue past current phase without user input
- If you catch yourself being verbose, STOP and provide only required output
- If you catch yourself about to skip a phase, STOP and go back to the correct phase
- If you catch yourself combining phases, STOP and perform only the current phase


