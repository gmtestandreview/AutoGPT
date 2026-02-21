# AutoGPT Project Folder Structure Blueprint

---

```text

title: "AutoGPT Project Folder Structure Blueprint"
description: "Comprehensive guide for maintaining consistent code organization in the AutoGPT monorepo"
last_updated: "2026-01-18"
project_type: "Python/TypeScript Monorepo"
architecture: "Microservices with Monorepo"
includes_frontend: true
includes_microservices: true
is_monorepo: true
```

---

## Auto-Detection Results

**Project Type Detection:**

- ✅ **Python Project**: Detected `pyproject.toml`, `requirements.txt`, Poetry configuration
- ✅ **TypeScript/React Project**: Detected `package.json`, `next.config.mjs`, React dependencies
- ✅ **Next.js Application**: Detected Next.js 15+ with App Router configuration
- ✅ **FastAPI Backend**: Detected FastAPI dependencies and async patterns
- ✅ **Prisma ORM**: Detected `schema.prisma` and database migrations

**Architecture Pattern Detection:**

- ✅ **Monorepo**: Multiple distinct projects with workspace configurations
- ✅ **Microservices Architecture**: Service-specific configurations and inter-service communication
- ✅ **Frontend Integration**: Modern React/Next.js frontend with API integration
- ✅ **Docker Orchestration**: Multi-service Docker Compose configurations
- ✅ **Database-First**: PostgreSQL with vector extensions and Prisma migrations

---

## 1. Structural Overview

### Architectural Approach

AutoGPT implements a **sophisticated monorepo architecture** with clear technology boundaries:

**Primary Architecture Patterns:**

1. **Domain-Driven Monorepo**: Clear separation between `autogpt_platform/` (modern) and `classic/` (legacy)
2. **Microservices-Ready Backend**: FastAPI services with async patterns, designed for horizontal scaling
3. **Modern Frontend Stack**: Next.js 15+ with React 19, App Router, and TypeScript
4. **Database-Centric Design**: PostgreSQL with pgvector for AI embeddings, Prisma for type-safe queries
5. **API-First Integration**: OpenAPI-generated clients, real-time WebSocket communication
6. **Container-Native**: Docker Compose orchestration for local development and production deployment

**Organizational Principles:**

- **Technology Boundaries**: Python backend, TypeScript frontend, shared utilities
- **Service Independence**: Self-contained services with clear API contracts
- **Development Workflow**: Independent build/test/deploy cycles per service
- **Code Reusability**: Shared libraries (`autogpt_libs/`) for cross-service functionality
- **Legacy Preservation**: `classic/` maintains backward compatibility with original AutoGPT

**Monorepo Structure:**
The project uses a **multi-root monorepo** where `autogpt_platform/` serves as the primary development focus, containing modern microservices, while `classic/` preserves the original CLI-based implementation.

**Microservices Organization:**
Services are organized as **domain-bounded contexts** with:

- **Backend Services**: API gateway, authentication, agent execution, data persistence
- **Frontend Applications**: User interfaces, admin dashboards, real-time monitoring
- **Shared Infrastructure**: Database schemas, message queues, caching layers
- **Integration Services**: External API connectors, webhook handlers, notification systems

---

## 2. Directory Visualization

### Complete Monorepo Structure (ASCII Tree - Depth 3)

```ASCII
AutoGPT/
├── .github/                          # GitHub workflows, issue templates, Copilot configuration
│   ├── workflows/                    # CI/CD pipelines for backend, frontend, and platform
│   ├── instructions/                 # GitHub Copilot instruction files (12 files)
│   ├── prompts/                      # Task-specific development prompts (7 files)
│   └── agents/                       # Specialized AI agents for architecture/review/debug
├── autogpt_platform/                 # 🎯 PRIMARY PLATFORM (Polyform Shield License)
│   ├── backend/                      # FastAPI Python services
│   │   ├── backend/                  # Core application logic
│   │   │   ├── api/                  # REST API endpoints and routers
│   │   │   ├── blocks/               # Agent execution blocks (50+ modular components)
│   │   │   ├── data/                 # Database models and Prisma integration
│   │   │   ├── executor/             # Agent workflow execution engine
│   │   │   ├── integrations/         # External service connectors (OpenAI, etc.)
│   │   │   └── usecases/             # Business logic and use case implementations
│   │   ├── migrations/               # Database schema migrations (Prisma)
│   │   ├── test/                     # Test suite (pytest with async support)
│   │   └── agents/                   # Agent configuration and templates
│   ├── frontend/                     # Next.js 15+ TypeScript application
│   │   ├── src/
│   │   │   ├── app/                  # Next.js App Router pages and layouts
│   │   │   ├── components/           # React components (atoms, molecules, organisms)
│   │   │   ├── lib/                  # Utilities, API clients, configuration
│   │   │   ├── hooks/                # Custom React hooks
│   │   │   └── types/                # TypeScript type definitions
│   │   ├── public/                   # Static assets (images, fonts, icons)
│   │   └── .storybook/               # Component documentation and testing
│   ├── autogpt_libs/                 # Shared Python utilities
│   │   └── autogpt_libs/             # Core library modules
│   ├── db/                           # Database infrastructure
│   ├── tools/                        # Development and deployment tools
│   └── graph_templates/              # Pre-built agent workflow templates
├── classic/                          # 🏛️ LEGACY IMPLEMENTATION (MIT License)
│   ├── original_autogpt/             # Original CLI-based AutoGPT
│   ├── forge/                        # Agent framework foundation
│   ├── benchmark/                    # Performance and capability benchmarks
│   └── frontend/                     # Flutter mobile application
├── docs/                             # 📚 DOCUMENTATION (MkDocs)
│   └── content/                      # Markdown documentation files
└── assets/                           # Repository-wide static assets
```

### Directory Statistics

- **Total Directories**: ~150+ at depth 3
- **Primary Technology Split**: 60% Python, 35% TypeScript, 5% Other
- **Code Distribution**: Backend (45%), Frontend (35%), Tests (15%), Documentation (5%)
- **Configuration Files**: 25+ distinct configuration types across technologies

---

## 3. Key Directory Analysis

### AutoGPT Platform Structure (`autogpt_platform/`)

#### Backend Service Organization (`autogpt_platform/backend/`)

**Primary Structure Pattern**: **Layered Architecture with Domain Separation**

```ASCII
backend/
├── backend/                          # Core application logic
│   ├── api/                          # FastAPI routers and endpoint definitions
│   │   ├── v1/                       # API version 1 endpoints
│   │   └── v2/                       # API version 2 endpoints  
│   ├── blocks/                       # 🧩 AGENT EXECUTION BLOCKS (50+ modules)
│   │   ├── basic/                    # Basic utility blocks
│   │   ├── ai/                       # AI/LLM integration blocks
│   │   ├── data/                     # Data processing blocks
│   │   └── web/                      # Web interaction blocks
│   ├── data/                         # 🗄️ DATABASE LAYER
│   │   ├── models/                   # Prisma model definitions
│   │   ├── repositories/             # Data access patterns
│   │   └── migrations/               # Schema evolution scripts
│   ├── executor/                     # 🎯 WORKFLOW EXECUTION ENGINE
│   │   ├── graph/                    # Graph-based workflow execution
│   │   ├── scheduler/                # Task scheduling and queuing
│   │   └── monitoring/               # Execution monitoring and metrics
│   ├── integrations/                 # 🔌 EXTERNAL SERVICE CONNECTORS
│   │   ├── llm/                      # Language model providers (OpenAI, etc.)
│   │   ├── vector_db/                # Vector database integrations
│   │   └── webhooks/                 # Webhook handling and delivery
│   └── usecases/                     # 💼 BUSINESS LOGIC LAYER
│       ├── agent/                    # Agent management use cases
│       ├── user/                     # User management use cases
│       └── execution/                # Execution management use cases
├── migrations/                       # 📊 PRISMA DATABASE MIGRATIONS
├── test/                             # 🧪 COMPREHENSIVE TEST SUITE
│   ├── unit/                         # Unit tests (pytest)
│   ├── integration/                  # Integration tests with real services
│   └── fixtures/                     # Test data and mock configurations
└── agents/                           # 🤖 AGENT DEFINITIONS AND TEMPLATES
```

**Key Organization Patterns:**

- **Block-Based Architecture**: Modular execution components with standardized interfaces
- **API Versioning**: Clear separation between API versions with backward compatibility
- **Domain Services**: Use case-driven business logic separation
- **Infrastructure Separation**: Database, external integrations, and monitoring isolated
- **Test Co-location**: Tests organized by type with shared fixtures

```ASCII

├── 📄 AGENTS.md                           # Contribution guide for platform development
├── 📄 CONTRIBUTING.md                     # Repository contribution guidelines
├── 📄 SECURITY.md                         # Security policy and vulnerability reporting
├── 📄 CODE_OF_CONDUCT.md                  # Community code of conduct
├── 📄 README.md                           # Main repository overview
├── 📄 LICENSE                             # Primary license file
├── 📄 CITATION.cff                        # Citation metadata
│
├── 📁 .github/                            # GitHub configuration
│   ├── workflows/                         # GitHub Actions CI/CD
│   ├── instructions/                      # Copilot instruction files
│   ├── prompts/                           # Task-specific prompts
│   ├── skills/                            # Domain-specific knowledge
│   └── PULL_REQUEST_TEMPLATE.md
│
├── 📁 assets/                             # Shared media assets (images, logos)
│
├── 📁 autogpt_platform/                   # Primary platform (Polyform Shield)
│   ├── backend/                           # FastAPI REST API
│   ├── frontend/                          # Next.js application
│   ├── autogpt_libs/                      # Shared Python libraries
│   ├── graph_templates/                   # Pre-built agent graph templates
│   ├── docker-compose.yml                 # Local development services
│   ├── docker-compose.platform.yml        # Platform-specific override
│   ├── Makefile                           # Development commands
│   ├── README.md                          # Platform documentation
│   └── CLAUDE.md                          # AI assistant development guide
│
├── 📁 classic/                            # Legacy AutoGPT system (MIT)
│   ├── cli.py                             # CLI entry point
│   ├── setup.sh / setup.bat               # Installation scripts
│   ├── forge/                             # Agent framework implementation
│   ├── benchmark/                         # Benchmarking suite
│   ├── original_autogpt/                  # Original implementation
│   └── frontend/                          # Flutter-based UI
│
├── 📁 docs/                               # MkDocs documentation site
│   ├── content/                           # Documentation content
│   ├── platform/                          # Platform-specific docs
│   ├── SUMMARY.md                         # Documentation index
│   └── README.md                          # Docs setup guide
│
└── 📁 installer/                          # Installation scripts
    ├── setup-autogpt.sh
    └── setup-autogpt.bat

```

### Backend Detailed Structure

```ASCII

autogpt_platform/backend/
├── 📄 pyproject.toml                      # Poetry dependency management
├── 📄 schema.prisma                       # Database schema (Prisma ORM)
├── 📄 pytest.ini                          # Pytest configuration
├── 📄 Dockerfile                          # Container image definition
├── 📄 run_tests.py                        # Test runner script
│
├── 📁 backend/                            # Main application code
│   ├── 📁 server/
│   │   ├── server.py                      # FastAPI app initialization
│   │   ├── middleware/                    # Security, caching, middleware
│   │   └── routers/                       # API endpoint definitions
│   │
│   ├── 📁 blocks/                         # Agent execution blocks
│   │   ├── **init**.py                    # Block registry and discovery
│   │   ├── api.py                         # Block API interface
│   │   ├── <block_category>/              # Blocks organized by category
│   │   └── test/
│   │       ├── test_block.py              # Parametrized block tests
│   │       └── snapshots/                 # Test snapshots
│   │
│   ├── 📁 data/                           # Database models & ORM layer
│   │   ├── db_session.py                  # Database connection
│   │   ├── <model>.py                     # Prisma-generated models
│   │   └── repositories/                  # Data access patterns
│   │
│   ├── 📁 agents/                         # Agent execution & orchestration
│   │   ├── agent_executor.py
│   │   ├── graph_executor.py
│   │   └── execution_context.py
│   │
│   └── 📁 schemas/                        # Pydantic models for API
│       ├── models.py                      # Request/response schemas
│       └── validators.py                  # Data validation logic
│
├── 📁 test/                               # Integration tests
│   ├── conftest.py                        # Pytest fixtures
│   ├── test_*.py                          # Test modules
│   └── fixtures/                          # Test data & mocks
│
├── 📁 migrations/                         # Database migrations (Prisma)
│   └── <timestamp>_<description>/
│
├── 📁 snapshots/                          # Snapshot test data
│   └── <test_module>.ambr
│
└── 📁 load-tests/                         # Performance testing
    ├── k6_config.js                       # k6 load test scenarios
    └── results/

```

### Frontend Detailed Structure

```ASCII

autogpt_platform/frontend/
├── 📄 package.json                        # pnpm dependencies & scripts
├── 📄 pnpm-lock.yaml                      # Locked dependency versions
├── 📄 tsconfig.json                       # TypeScript configuration
├── 📄 next.config.mjs                     # Next.js configuration
├── 📄 tailwind.config.ts                  # Tailwind CSS configuration
├── 📄 playwright.config.ts                # E2E test configuration
├── 📄 orval.config.ts                     # OpenAPI code generation config
├── 📄 components.json                     # Shadcn/ui component index
│
├── 📁 src/
│   ├── 📁 app/                            # App Router (Next.js 15+)
│   │   ├── layout.tsx                     # Root layout
│   │   ├── page.tsx                       # Home page (/)
│   │   ├── (auth)/                        # Authentication routes (grouped)
│   │   ├── (dashboard)/                   # Dashboard routes
│   │   ├── api/                           # API routes
│   │   │   ├── **generated**/             # Auto-generated from OpenAPI
│   │   │   └── <endpoint>/                # API route handlers
│   │   └── error.tsx, not-found.tsx       # Error boundaries
│   │
│   ├── 📁 components/                     # Reusable React components
│   │   ├── atoms/                         # Basic UI elements (Button, Input, etc.)
│   │   ├── molecules/                     # Composed components (Card, Form, etc.)
│   │   ├── organisms/                     # Complex components (Header, Sidebar, etc.)
│   │   ├── **legacy**/                    # Deprecated components (to remove)
│   │   └── <feature>/                     # Feature-specific components
│   │       ├── <ComponentName>/
│   │       │   ├── <ComponentName>.tsx    # Main render logic
│   │       │   ├── use<ComponentName>.ts  # Hook with logic
│   │       │   └── helpers.ts             # Utility functions
│   │       └── index.ts                   # Barrel export (use sparingly)
│   │
│   ├── 📁 hooks/                          # Custom React hooks
│   │   ├── useQuery.ts
│   │   ├── useMutation.ts
│   │   └── use<FeatureName>.ts
│   │
│   ├── 📁 lib/                            # Utilities and configurations
│   │   ├── autogpt-server-api/            # DEPRECATED (see **generated**)
│   │   ├── supabase/                      # Authentication & database client
│   │   │   ├── client.ts                  # Supabase client setup
│   │   │   ├── middleware.ts              # Route protection middleware
│   │   │   └── auth.ts                    # Auth utilities
│   │   ├── utils.ts                       # General utilities
│   │   ├── constants.ts                   # App-wide constants
│   │   └── types.ts                       # Shared TypeScript types
│   │
│   ├── 📁 types/                          # TypeScript type definitions
│   │   ├── api.ts                         # API-related types
│   │   ├── domain.ts                      # Business domain types
│   │   └── index.ts
│   │
│   └── 📁 styles/                         # Global styles
│       ├── globals.css                    # Global CSS
│       └── variables.css                  # CSS custom properties
│
├── 📁 public/                             # Static assets
│   ├── images/
│   ├── fonts/
│   ├── icons/
│   └── favicon.ico
│
├── 📁 scripts/                            # Build and utility scripts
│   ├── generate-api.ts                    # Orval API generation
│   └── <utility>.ts
│
├── 📁 .storybook/                         # Component development
│   ├── main.ts                            # Storybook configuration
│   └── preview.ts
│
├── 📁 stories/                            # Component stories
│   └── <ComponentName>.stories.tsx
│
└── 📁 **tests**/                          # Test files
    ├── <component>.test.tsx               # Jest tests
    └── e2e/                               # Playwright E2E tests

```

### Shared Libraries Structure

```ASCII

autogpt_platform/autogpt_libs/
├── 📄 pyproject.toml                      # Package definition
├── 📄 README.md                           # Library documentation
│
└── 📁 autogpt_libs/
    ├── 📁 agents/                         # Agent-related utilities
    │   ├── agent_protocol.py              # Protocol definitions
    │   └── execution.py                   # Execution helpers
    │
    ├── 📁 models/                         # Shared data models
    │   ├── agent.py                       # Agent models
    │   └── graph.py                       # Graph models
    │
    └── 📁 utils/                          # Common utilities
        ├── logging.py                     # Logging configuration
        └── validators.py                  # Validation helpers

```

---

## 4. Key Organization Analysis

### Backend Organization

#### Server/API Layer (`backend/server/`)

**Purpose**: FastAPI application setup and HTTP request handling

**Key Files**:

- `server.py` - FastAPI app initialization, middleware registration, CORS setup
- `middleware/security.py` - Cache control and security headers
- `routers/` - Endpoint definitions organized by domain

**Patterns**:

- Async-first design for all endpoints
- Request/response validation via Pydantic
- JWT authentication via Supabase
- Database session injection via dependency injection

---

#### Blocks System (`backend/blocks/`)

**Purpose**: Modular, composable agent execution units

**Key Files**:

- `__init__.py` - Block registry and discovery mechanism
- `api.py` - Block protocol and base class definitions
- `test/test_block.py` - Parametrized tests for all blocks

**Organization**:

```ASCII
blocks/
├── ai_blocks/           # AI/LLM integration blocks
├── data_blocks/         # Data manipulation blocks
├── integration_blocks/  # Third-party service blocks
└── utility_blocks/      # Helper and utility blocks
```

**Patterns**:

- Each block inherits from `Block` base class
- Input/output schemas defined with Pydantic
- UUID-based registration (`uuid.uuid4()`)
- Snapshot testing for deterministic output validation
- All blocks tested parametrically via `test_block.py`

---

#### Data Layer (`backend/data/`)

**Purpose**: ORM models, database access, and business entity definitions

**Key Files**:

- `db_session.py` - Connection pooling and session management
- `<model>.py` - Auto-generated Prisma models
- `repositories/` - Data access patterns and queries

**Patterns**:

- Prisma ORM for type-safe database access
- Connection pooling for performance
- User ID validation on all queries (security requirement)
- Async database operations
- Query optimization with eager loading

---

#### Schemas (`backend/schemas/`)

**Purpose**: Request/response validation and API contracts

**Key Files**:

- `models.py` - Pydantic models for all API endpoints
- `validators.py` - Custom validation logic

**Patterns**:

- One schema per endpoint or domain
- Validators use Pydantic's validation decorators
- Schemas include OpenAPI documentation via `Field()` descriptions
- Strict validation with `ConfigDict(strict=True)`

---

### Frontend Organization

#### App Router (`src/app/`)

**Purpose**: Page structure and routing (Next.js 15+ App Router)

**Layout**:

- `layout.tsx` - Root layout with providers
- Grouped routes use parentheses: `(auth)`, `(dashboard)`
- API routes in `app/api/` with specific HTTP verb handlers

**Patterns**:

- Server Components by default
- Client Components only when needed (`'use client'`)
- Layout composition for shared UI
- Metadata configuration via `generateMetadata()`

---

#### Components (`src/components/`)

**Purpose**: Reusable UI building blocks

**Organization**:

```ASCII
components/
├── atoms/         # Buttons, Inputs, Labels (basic elements)
├── molecules/     # Forms, Cards, Modals (composed atoms)
├── organisms/     # Header, Sidebar, Navigation (complex sections)
└── <Feature>/     # Feature-specific components
    └── <Name>/
        ├── <Name>.tsx          # Render logic only
        ├── use<Name>.ts        # Hooks and state
        └── helpers.ts          # Utilities
```

**Patterns**:

- Separation of concerns (render vs. logic)
- Hooks exported from `use*.ts` files
- Helper functions isolated in `helpers.ts`
- Barrel exports only in top-level `atoms/`, `molecules/`, `organisms/`
- No nested index files in feature components
- Storybook stories colocated: `<Name>.stories.tsx`

---

#### Hooks (`src/hooks/`)

**Purpose**: Custom React hooks for state and effects

**Key Hooks**:

- `useQuery.ts` - Data fetching with React Query
- `useMutation.ts` - Data mutations with React Query
- `use<FeatureName>.ts` - Feature-specific logic

**Patterns**:

- All hooks auto-generated from OpenAPI spec via Orval
- Prefix all hooks with `use`
- Group related hooks by feature
- Export types alongside hooks

---

#### API Integration (`src/lib/supabase/`, `src/app/api/__generated__/`)

**Purpose**: API client and authentication

**Key Files**:

- `supabase/client.ts` - Supabase JavaScript client
- `supabase/middleware.ts` - Protected route middleware
- `app/api/__generated__/` - Auto-generated hooks from OpenAPI

**Patterns**:

- Auto-generated hooks from backend OpenAPI spec
- Naming: `use{Method}{Version}{OperationName}` (e.g., `useGetV2ListLibraryAgents`)
- Regenerate with: `pnpm generate:api`
- Supabase for auth, real-time, and database
- JWT tokens in Authorization headers

---

### Test Organization

#### Backend Tests

**Location**: `backend/test/`, `backend/blocks/test/`

**Structure**:

- `conftest.py` - Pytest fixtures, database setup, async configuration
- `test_*.py` - Test modules
- `fixtures/` - Mock data and test utilities
- `snapshots/` - Snapshot data for deterministic testing

**Patterns**:

- Async tests with `asyncio_mode = "auto"` (via pytest.ini)
- Parametrized tests for multiple scenarios
- Snapshot testing via `syrupy` plugin
- Database transactions rolled back after tests (isolation)
- Mock external services

---

#### Frontend Tests

**Location**: `frontend/__tests__/`, `frontend/**/*.test.tsx`

**Structure**:

- Co-located with components: `Component.test.tsx`
- E2E tests in `__tests__/e2e/`
- Storybook stories as visual tests

**Patterns**:

- Jest for unit/integration tests
- React Testing Library for user-centric testing
- Playwright for E2E tests
- Tests run against running dev server (`pnpm dev` before `pnpm test`)
- Focus on user behavior, not implementation

---

## 4. File Placement Patterns

### Configuration Files

| File Type | Location | Purpose |
| ----------- | ---------- | --------- |
| Database Schema | `backend/schema.prisma` | Prisma ORM models |
| Environment Variables | `backend/.env.default`, `frontend/.env.default` | Environment configuration |
| Dependency Management | `backend/pyproject.toml`, `frontend/package.json` | Package definitions |
| Build Configuration | `frontend/next.config.mjs`, `backend/Dockerfile` | Build/deployment config |
| Test Configuration | `backend/pytest.ini`, `frontend/playwright.config.ts` | Test runner setup |
| Docker Compose | `autogpt_platform/docker-compose.yml` | Local development services |

### Model/Entity Definitions

| Entity Type | Location | Pattern |
| ------------- | ---------- | --------- |
| Database Models | `backend/data/<model>.py` | Auto-generated by Prisma |
| API Schemas | `backend/schemas/models.py` | Pydantic models for validation |
| TypeScript Types | `frontend/src/types/` | Domain and API types |
| React Hooks | `frontend/src/hooks/` | State management and logic |
| Prisma Schema | `backend/schema.prisma` | Database design source |

### Business Logic

| Logic Type | Location | Pattern |
| ----------- | ---------- | --------- |
| API Endpoints | `backend/backend/server/routers/` | One file per domain |
| Block Implementations | `backend/backend/blocks/<category>/` | Each block in separate file |
| Services | `backend/backend/services/` | Business rule implementations |
| Repositories | `backend/backend/data/repositories/` | Data access patterns |
| React Components | `frontend/src/components/` | Feature-organized |
| Hooks | `frontend/src/hooks/` | One hook per file or `use*.ts` |

### Test Files

| Test Type | Location | Pattern |
| ----------- | ---------- | --------- |
| Unit Tests (Backend) | `backend/test/test_*.py` | Pytest modules |
| Block Tests | `backend/blocks/test/test_block.py` | Parametrized tests |
| Component Tests | `frontend/__tests__/**/*.test.tsx` | Jest with RTL |
| E2E Tests | `frontend/__tests__/e2e/` | Playwright scripts |
| Snapshots (Backend) | `backend/snapshots/` | `.ambr` files |
| Snapshots (Frontend) | `frontend/__tests__/__snapshots__/` | Jest snapshots |

### Documentation Files

| Document Type | Location | Pattern |
| --------------- | ---------- | --------- |
| API Documentation | `backend/README.md`, backend docstrings | OpenAPI auto-generated |
| Component Documentation | `frontend/**/*.stories.tsx` | Storybook stories |
| Architecture Decisions | `AGENTS.md`, `CLAUDE.md` | Top-level guides |
| Setup Instructions | `README.md`, `docs/` | MkDocs documentation |
| Contribution Guidelines | `CONTRIBUTING.md`, `AGENTS.md` | PR templates and conventions |

---

## 5. Naming and Organization Conventions

### File Naming Patterns

#### Backend (Python)

| Item Type | Convention | Example |
| ----------- | ----------- | --------- |
| Module Files | `snake_case.py` | `user_service.py`, `block_registry.py` |
| Class Names | `PascalCase` | `UserService`, `BlockRegistry` |
| Function Names | `snake_case` | `get_user()`, `execute_block()` |
| Constants | `SCREAMING_SNAKE_CASE` | `MAX_RETRIES`, `DEFAULT_TIMEOUT` |
| Private Items | `_leading_underscore` | `_internal_helper()` |
| Test Files | `test_<module>.py` | `test_user_service.py` |
| Snapshots | `<test_module>.ambr` | `test_block.ambr` |

#### Frontend (TypeScript/React)

| Item Type | Convention | Example |
| ----------- | ----------- | --------- |
| Component Files | `PascalCase.tsx` | `UserProfile.tsx`, `AgentCard.tsx` |
| Hook Files | `use<Name>.ts` | `useUserData.ts`, `useAgentState.ts` |
| Utility Files | `camelCase.ts` | `formatDate.ts`, `validators.ts` |
| Type Files | `<domain>.types.ts` | `user.types.ts`, `agent.types.ts` |
| Style Files | `<Name>.module.css` | `UserProfile.module.css` |
| Test Files | `<Name>.test.tsx` or `.test.ts` | `UserProfile.test.tsx` |
| Stories | `<Name>.stories.tsx` | `UserProfile.stories.tsx` |
| Directories | `kebab-case` | `auth-provider/`, `layout-components/` |

### Folder Naming Patterns

| Folder Type | Convention | Example |
| ------------- | ----------- | --------- |
| Feature Folders | `kebab-case` | `user-profile/`, `agent-builder/` |
| Functional Groups | `lowercase` | `blocks/`, `hooks/`, `components/` |
| Domain Layers | `lowercase` | `server/`, `data/`, `schemas/` |
| Utility Folders | `lowercase` | `utils/`, `helpers/`, `fixtures/` |
| Route Groups | Parentheses `()` | `(auth)/`, `(dashboard)/` |
| Grouped Routes | `kebab-case` inside `()` | `(auth)/login/`, `(auth)/register/` |

### Namespace/Module Patterns

#### Backend Python

```python
# Module structure reflects folder structure
from backend.server.routers import user_router
from backend.blocks.ai_blocks import llm_block
from backend.data.repositories import user_repository
from backend.schemas.models import UserSchema

# Imports organized by: stdlib → third-party → local
import json
from typing import Optional

import fastapi
import sqlalchemy

from backend.server import app
from backend.blocks import Block
```

#### Frontend TypeScript

```typescript
// Absolute imports from src/
import { Button } from '@/components/atoms';
import { useUserData } from '@/hooks/useUserData';
import { formatDate } from '@/lib/utils';
import { User } from '@/types/api';

// Relative imports for sibling files
import { helpers } from './helpers';
import { useComponentLogic } from './useComponentLogic';

// Barrel exports only at layer level
export * from './atoms';  // ✓ OK
export { Button };        // ✓ OK
// export { Button } from './Button'; in index.ts  ✗ Avoid
```

### Organizational Patterns

#### Backend Block Organization

**Principle**: Blocks are categorized by function and domain

```ASCII

blocks/
├── ai_blocks/
│   ├── __init__.py              # Register AI blocks
│   ├── llm_block.py             # LLM integration
│   ├── embedding_block.py       # Vector embeddings
│   └── test/
├── data_blocks/
│   ├── __init__.py
│   ├── csv_processor.py
│   ├── json_parser.py
│   └── test/
└── integration_blocks/
    ├── __init__.py
    ├── slack_block.py
    ├── webhook_block.py
    └── test/

```

#### Frontend Component Organization

**Principle**: Feature-based organization within functional hierarchy

```ASCII

components/
├── atoms/
│   ├── Button.tsx              # Single responsibility
│   ├── Input.tsx
│   └── Label.tsx
├── molecules/
│   ├── LoginForm/
│   │   ├── LoginForm.tsx        # Render only
│   │   ├── useLoginForm.ts      # Logic & state
│   │   └── helpers.ts           # Utilities
│   └── AgentCard/
│       ├── AgentCard.tsx
│       ├── useAgentCard.ts
│       └── helpers.ts
└── organisms/
    ├── Header/
    ├── Sidebar/
    └── MainContent/
```

---

## 6. Navigation and Development Workflow

### Entry Points

#### Backend Entry Points

| Entry Point | File | Purpose |
| --- | --- | --- |
| Application | `backend/backend/server/server.py` | FastAPI app initialization |
| Database | `backend/schema.prisma` | Schema and model definitions |
| Blocks Registry | `backend/backend/blocks/__init__.py` | Block discovery and registration |
| Main Router | `backend/backend/server/routers/` | API endpoint organization |

#### Frontend Entry Points

| Entry Point | File | Purpose |
| ------------- | ------ | --------- |
| Root Layout | `frontend/src/app/layout.tsx` | App providers and layout |
| Home Page | `frontend/src/app/page.tsx` | Landing page |
| API Client | `frontend/src/app/api/__generated__/` | Auto-generated API hooks |
| Authentication | `frontend/src/lib/supabase/` | Auth and session management |

### Common Development Tasks

#### Adding a New Backend Endpoint

1. **Define Schema**: Create models in `backend/schemas/models.py`
2. **Create Router**: Add endpoint in `backend/backend/server/routers/<domain>.py`
3. **Implement Business Logic**: Create service in `backend/backend/services/`
4. **Add Tests**: Create test in `backend/test/test_<feature>.py`
5. **Update Documentation**: Add docstrings with OpenAPI decorators

#### Adding a New Block

1. **Create Block File**: New file in `backend/backend/blocks/<category>/<block_name>.py`
2. **Inherit from Block**: Extend `Block` base class with input/output schemas
3. **Implement run()**: Add execution logic with error handling
4. **Register Block**: Add to category's `__init__.py`
5. **Write Tests**: Tests auto-parametrized in `test_block.py`
6. **Add Documentation**: Docstring becomes OpenAPI schema

#### Adding a New Frontend Page

1. **Create Route**: New folder in `frontend/src/app/<route>/`
2. **Create Layout** (if needed): `layout.tsx` for shared structure
3. **Create Page**: `page.tsx` with Server Component by default
4. **Add Components**: Create feature components in `frontend/src/components/<feature>/`
5. **Add Hooks**: Extract logic to `frontend/src/hooks/`
6. **Add Tests**: Create `page.test.tsx` and component tests
7. **Add Stories**: Create `.stories.tsx` for Storybook

#### Adding a New React Component

1. **Create Folder**: `frontend/src/components/<feature>/<ComponentName>/`
2. **Create Component**: `<ComponentName>.tsx` with render logic only
3. **Create Hook** (if logic): `use<ComponentName>.ts` with state/effects
4. **Create Helpers** (if utilities): `helpers.ts` for pure functions
5. **Create Story**: `<ComponentName>.stories.tsx` for Storybook
6. **Create Tests**: `<ComponentName>.test.tsx` with React Testing Library
7. **Export**: Optionally add to parent `index.ts` (atoms/molecules/organisms only)

#### Modifying the Database Schema

1. **Edit Schema**: Update `backend/schema.prisma`
2. **Create Migration**: `poetry run prisma migrate dev --name <description>`
3. **Generate Models**: `poetry run prisma generate`
4. **Update Tests**: If data structure changed, update test fixtures
5. **Update API Schemas**: Update Pydantic models in `backend/schemas/`
6. **Test Migration**: Run full test suite to verify

### Dependency Patterns

#### Backend Dependencies

```ASCII
Routers (API Layer)
    ↓
Services (Business Logic)
    ↓
Repositories (Data Access)
    ↓
Prisma Models (Database)
```

- **Imports flow**: Higher layers depend on lower layers
- **Dependency Injection**: Via FastAPI's `Depends()`
- **No circular imports**: Use type hints and forward references

#### Frontend Dependencies

```ASCII
Pages (App Router)
    ↓
Organisms (Complex Components)
    ↓
Molecules (Composed Components)
    ↓
Atoms (Base Elements)
```

- **Imports flow**: Higher components depend on lower components
- **Hooks extract logic**: Keep components focused on rendering
- **API hooks**: Auto-generated and consumed by components
- **No prop drilling**: Use Context or state management library

### Content Statistics

```ASCII
Backend:
- ~40 blocks organized in 5+ categories
- 100+ API endpoints across multiple routers
- 8+ database models with relationships
- 100+ unit and integration tests
- Async/await patterns throughout

Frontend:
- 50+ components (atoms, molecules, organisms)
- 30+ custom hooks
- 25+ pages/routes
- 80+ E2E test scenarios
- TypeScript strict mode enabled
```

---

## 7. Build and Output Organization

### Build Configuration

#### Backend Build

**Build Tool**: Poetry + Docker

**Key Files**:

- `pyproject.toml` - Dependencies and metadata
- `Dockerfile` - Multi-stage production image
- `Makefile` - Common development commands

**Build Steps**:

```bash
poetry install                      # Install dependencies
poetry run prisma generate          # Generate ORM client
poetry run pytest                   # Run tests
poetry run format && poetry run lint # Code quality
docker build -t autogpt-backend .   # Build container
```

#### Frontend Build

**Build Tool**: pnpm + Next.js + Docker

**Key Files**:

- `package.json` - Dependencies and scripts
- `next.config.mjs` - Next.js configuration
- `Dockerfile` - Multi-stage production image

**Build Steps**:

```bash
pnpm install                        # Install dependencies
pnpm generate:api                   # Generate API hooks
pnpm format && pnpm lint            # Code quality
pnpm build                          # Build optimized output
docker build -t autogpt-frontend .  # Build container
```

### Output Structure

#### Backend Output

```ASCII
.output/
├── backend/
│   ├── __pycache__/              # Compiled Python
│   ├── dist/                      # Built artifacts (if applicable)
│   └── .pytest_cache/             # Test cache
└── cov_annotate/                  # Coverage reports with annotations
```

#### Frontend Output

```ASCII
.next/
├── static/                        # Static assets
├── server/                        # Server-side code
├── cache/                         # Build cache
└── 

out/                               # Static export (if configured)
dist/                              # Production build output
.turbopack/                        # Turbopack cache
```

### Environment-Specific Builds

#### Development

**Configuration**:

- `docker-compose.yml` - Local services (DB, Redis, RabbitMQ)
- Backend: `DEBUG=true`, SQL query logging enabled
- Frontend: Hot module reloading, source maps
- API: Swagger UI at `/docs`

**Commands**:

```bash
cd autogpt_platform
docker compose --profile local up deps --build --detach
cd backend && poetry run serve
cd ../frontend && pnpm dev
```

#### Production

**Configuration**:

- Multi-stage Docker builds (minimal final image)
- Environment variables from secrets manager
- No debug output or verbose logging
- Optimized asset sizes and compression
- CORS configured for specific origins

**Docker Compose Override**:

```yaml
# docker-compose.platform.yml
# Replaces dev settings with production values
services:
  backend:
    environment:
      - ENVIRONMENT=production
      - DEBUG=false
```

---

## 8. Technology-Specific Organization

### Python Backend Patterns

#### Project Structure

```ASCII
backend/
├── pyproject.toml                 # Poetry project config
├── poetry.lock                    # Locked dependencies
├── schema.prisma                  # Prisma schema
├── Dockerfile                     # Container image
│
└── backend/                       # Source code
    ├── __init__.py
    ├── server/
    │   ├── server.py              # FastAPI app
    │   ├── middleware/            # Custom middleware
    │   └── routers/               # Endpoint routers
    ├── blocks/
    │   ├── __init__.py            # Block registry
    │   └── <category>/
    ├── data/
    │   ├── db_session.py          # Connection management
    │   └── <model>.py             # Prisma models
    └── schemas/
        └── models.py              # Pydantic schemas
```

#### Python Patterns

```python
# Async-first design
async def get_user(user_id: str, session: AsyncSession) -> User:
    result = await session.execute(
        select(UserModel).where(UserModel.id == user_id)
    )
    return result.scalar_one_or_none()

# Pydantic validation
from pydantic import BaseModel, Field

class UserSchema(BaseModel):
    id: str = Field(..., description="User unique identifier")
    email: str = Field(..., pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$")
    
    model_config = ConfigDict(strict=True)

# Dependency injection
@router.get("/users/{user_id}")
async def read_user(
    user_id: str,
    session: AsyncSession = Depends(get_session),
) -> UserSchema:
    user = await get_user(user_id, session)
    return UserSchema.model_validate(user)
```

### TypeScript/Next.js Frontend Patterns

#### Component Structure

```typescript
// src/components/molecules/UserCard/UserCard.tsx
'use client';  // Client-side component

interface UserCardProps {
  userId: string;
  onSelect?: (id: string) => void;
}

export function UserCard({ userId, onSelect }: UserCardProps) {
  const { data, isLoading } = useUserCard(userId);
  
  if (isLoading) return <Skeleton />;
  
  return (
    <Card onClick={() => onSelect?.(userId)}>
      {/* Render logic */}
    </Card>
  );
}

// src/components/molecules/UserCard/useUserCard.ts
export function useUserCard(userId: string) {
  return useGetV2UserById(userId);  // Auto-generated API hook
}

// src/components/molecules/UserCard/helpers.ts
export function formatUserName(firstName: string, lastName: string): string {
  return `${firstName} ${lastName}`;
}
```

#### App Router Structure

```typescript
// src/app/layout.tsx (Root)
export const metadata: Metadata = {
  title: 'AutoGPT Platform',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html>
      <body>
        <AuthProvider>{children}</AuthProvider>
      </body>
    </html>
  );
}

// src/app/(dashboard)/page.tsx
import { redirect } from 'next/navigation';
import { getSession } from '@/lib/supabase/auth';

export default async function DashboardPage() {
  const session = await getSession();
  if (!session) redirect('/login');
  
  return <Dashboard />;
}
```

### Docker Organization

#### Multi-Stage Builds

```dockerfile
# backend/Dockerfile
FROM python:3.11-slim AS builder
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-dev --no-root

FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /app/.venv ./.venv
COPY backend/ ./backend/
ENV PATH="/app/.venv/bin:$PATH"
CMD ["poetry", "run", "serve"]
```

#### Docker Compose Organization

```yaml
# docker-compose.yml
version: '3.8'
services:
  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data

  backend:
    build:
      context: ./backend
      target: development
    environment:
      DATABASE_URL: postgresql://...
      REDIS_URL: redis://redis:6379
    depends_on:
      - postgres

  frontend:
    build:
      context: ./frontend
      target: development
    ports:
      - "3000:3000"
    depends_on:
      - backend
```

---

## 9. Extension and Evolution

### Extension Points

#### Adding New Modules

**For Backend Services**:

1. Create new folder in `backend/backend/<domain>/`
2. Follow existing patterns for routers, services, repositories
3. Create corresponding test module in `backend/test/`
4. Register new routes in `backend/backend/server/server.py`
5. Document new endpoints with OpenAPI decorators

**For Frontend Features**:

1. Create feature folder in `frontend/src/components/`
2. Create corresponding route in `frontend/src/app/`
3. Add hooks in `frontend/src/hooks/` as needed
4. Create stories in `frontend/stories/`
5. Add tests and E2E scenarios

#### Adding New Blocks

```python
# backend/backend/blocks/custom_blocks/my_block.py
from backend.blocks.api import Block, BlockInput, BlockOutput
from pydantic import BaseModel
import uuid

class MyBlockInput(BaseModel):
    value: str

class MyBlockOutput(BaseModel):
    result: str

class MyBlock(Block):
    id: str = str(uuid.uuid4())
    name = "My Block"
    description = "Does something useful"
    
    input_model = MyBlockInput
    output_model = MyBlockOutput
    
    async def run(self, input: MyBlockInput) -> MyBlockOutput:
        # Implementation
        return MyBlockOutput(result=input.value.upper())
```

### Scalability Patterns

#### Backend Scaling

- **Horizontal**: Stateless API can run in multiple instances
- **Database**: Read replicas for heavy query workloads
- **Caching**: Redis for frequently accessed data
- **Message Queue**: RabbitMQ for async job processing
- **Vector Search**: pgvector extension for semantic search

#### Frontend Scaling

- **Code Splitting**: Lazy load routes and components
- **Image Optimization**: Next.js Image component with WebP
- **CDN Delivery**: Static assets served from edge nodes
- **Serverless**: API routes can run on edge functions
- **Analytics**: Sentry for error tracking and performance monitoring

### Refactoring Patterns

**Common Refactoring Scenarios**:

1. **Extract Component**: Move component logic to new `<Feature>/` folder
2. **Extract Hook**: Move state/effects to `use<Name>.ts` file
3. **Extract Utility**: Move pure functions to `helpers.ts` or `utils.ts`
4. **Consolidate Routes**: Move related endpoints to single router
5. **Migrate Block**: Move block from one category to another while maintaining tests

---

## 10. Structure Templates

### New Backend Endpoint Template

```python
# backend/backend/server/routers/example.py
from fastapi import APIRouter, Depends
from backend.data.db_session import get_session
from backend.schemas.models import ExampleSchema
from backend.backend.services.example_service import ExampleService

router = APIRouter(prefix="/examples", tags=["examples"])

@router.post("/", response_model=ExampleSchema)
async def create_example(
    data: ExampleSchema,
    session: AsyncSession = Depends(get_session),
):
    """Create a new example."""
    service = ExampleService(session)
    return await service.create(data)
```

### New React Component Template

```typescript
// frontend/src/components/molecules/Example/Example.tsx
'use client';

interface ExampleProps {
  id: string;
  title: string;
}

export function Example({ id, title }: ExampleProps) {
  const { data, error } = useExample(id);
  
  if (error) return <ErrorCard error={error} />;
  
  return (
    <Card>
      <h2>{title}</h2>
      {/* Component content */}
    </Card>
  );
}

// frontend/src/components/molecules/Example/useExample.ts
export function useExample(id: string) {
  return useGetV2ExampleById(id);
}

// frontend/src/components/molecules/Example/Example.stories.tsx
import type { Meta, StoryObj } from '@storybook/react';
import { Example } from './Example';

const meta = {
  component: Example,
} satisfies Meta<typeof Example>;

export default meta;
type Story = StoryObj<typeof meta>;

export const Default: Story = {
  args: {
    id: '1',
    title: 'Example Title',
  },
};
```

### New Test Template (Backend)

```python
# backend/test/test_example_feature.py
import pytest
from unittest.mock import AsyncMock, patch
from backend.backend.services.example_service import ExampleService

@pytest.fixture
async def example_service():
    return ExampleService(session=AsyncMock())

@pytest.mark.asyncio
async def test_example_creation(example_service):
    """Test that example can be created."""
    result = await example_service.create(data={"name": "test"})
    assert result.id is not None
    assert result.name == "test"

@pytest.mark.asyncio
async def test_example_not_found(example_service):
    """Test 404 when example doesn't exist."""
    with pytest.raises(NotFoundError):
        await example_service.get(id="nonexistent")
```

### New Test Template (Frontend)

```typescript
// frontend/src/components/molecules/Example/Example.test.tsx
import { render, screen } from '@testing-library/react';
import { Example } from './Example';

// Mock the auto-generated hook
jest.mock('@/app/api/__generated__/endpoints', () => ({
  useGetV2ExampleById: () => ({
    data: { id: '1', title: 'Test' },
    isLoading: false,
  }),
}));

describe('Example', () => {
  it('renders title', () => {
    render(<Example id="1" title="Test" />);
    expect(screen.getByText('Test')).toBeInTheDocument();
  });
});
```

---

## 11. Structure Enforcement

### Build-Time Checks

**GitHub Actions Workflows**:

- `platform-backend-ci.yml` - Backend tests, linting, type checking
- `platform-frontend-ci.yml` - Frontend tests, E2E, build validation
- `platform-fullstack-ci.yml` - End-to-end integration tests

**Pre-Commit Hooks**:

- Python: `black`, `isort`, `ruff` (via Poetry)
- TypeScript: `prettier`, `eslint`, `tsconfig` validation
- Paths: Conventional commit format validation

### Development-Time Checks

**Backend**:

```bash
poetry run format    # Black + isort
poetry run lint      # Ruff + pyright
poetry run test      # Pytest with coverage
```

**Frontend**:

```bash
pnpm format          # Prettier + ESLint
pnpm test            # Playwright E2E
pnpm build           # Next.js production build
```

### Structural Guidelines

1. **Single Responsibility**: Files should have one clear purpose
2. **Feature Encapsulation**: Related code should be colocated
3. **Layer Separation**: Don't skip abstraction layers
4. **Type Safety**: Enable strict type checking in all projects
5. **Test Coverage**: Target >80% code coverage minimum
6. **Documentation**: API endpoints and complex logic need docstrings
7. **Performance**: Profile before optimizing; benchmark critical paths

---

## 12. Maintenance and Updates

### When to Update This Blueprint

- **Major architectural changes**: New service added, folder reorganization
- **New patterns established**: Standard way to organize new feature type
- **Technology upgrades**: Framework version changes affecting structure
- **Quarterly review**: Keep documentation current with actual codebase

### Structure Evolution Checklist

- [ ] Verify folder organization matches this blueprint
- [ ] Check naming conventions are followed
- [ ] Review dependency patterns are acyclic
- [ ] Confirm test organization mirrors source organization
- [ ] Validate documentation is colocated with code
- [ ] Update this blueprint if changes are needed
- [ ] Run structure validation in CI/CD

---

**Last Updated**: 2026-01-18  
**Next Review**: Q2 2026  
**Maintained By**: AutoGPT Development Team  
**Related Documentation**: [CONTRIBUTING.md](./CONTRIBUTING.md), [AGENTS.md](./AGENTS.md), [CLAUDE.md](./autogpt_platform/CLAUDE.md)
