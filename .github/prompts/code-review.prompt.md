---
title: "Code Review Checklist"
description: "Comprehensive code review guidelines for AutoGPT development"
category: "Code Quality"
tags: ["code-review", "quality", "standards", "best-practices"]
version: "1.0.0"
---

# Code Review Checklist

You are conducting a thorough code review for the AutoGPT platform. Use this comprehensive checklist to ensure code quality, security, and maintainability.

## Review Context

**Pull Request:** {PR_NUMBER}
**Author:** {AUTHOR}
**Files Changed:** {CHANGED_FILES}
**Type of Change:** {CHANGE_TYPE} (feature/bugfix/refactor/docs)

## 1. Code Quality & Style

### General Code Quality
- [ ] **Code is readable and self-documenting**
- [ ] **Functions are focused and single-purpose**
- [ ] **Variable and function names are descriptive**
- [ ] **No dead code or commented-out code blocks**
- [ ] **Consistent formatting** (run formatters: `poetry run format`, `pnpm format`)
- [ ] **No unnecessary complexity** or over-engineering

### Language-Specific Standards

#### Python Code
- [ ] **Follows PEP 8** style guidelines
- [ ] **Type hints** provided for function parameters and returns
- [ ] **Docstrings** follow PEP 257 conventions
- [ ] **Error handling** is comprehensive and appropriate
- [ ] **Async/await** used properly for I/O operations
- [ ] **No SQL injection** risks (using Prisma ORM properly)

#### TypeScript/React Code
- [ ] **Strict TypeScript** configuration followed
- [ ] **Proper component structure** (functional components with hooks)
- [ ] **Props interfaces** are well-defined
- [ ] **Hooks used correctly** with proper dependency arrays
- [ ] **No useEffect** without cleanup where needed
- [ ] **Performance considerations** (memo, useCallback where appropriate)

## 2. Architecture & Design

### Code Organization
- [ ] **Files in appropriate directories** following project structure
- [ ] **Imports organized** and using established patterns
- [ ] **Separation of concerns** maintained
- [ ] **DRY principle** followed (no unnecessary duplication)
- [ ] **Single responsibility** principle adhered to

### AutoGPT-Specific Patterns
- [ ] **Backend changes follow FastAPI** conventions
- [ ] **Database operations use Prisma ORM** patterns
- [ ] **Frontend uses generated API hooks** from `@/app/api/__generated__/`
- [ ] **Component structure** follows established patterns in `src/components/`
- [ ] **User ID validation** present in data layer changes (`data/*.py`)

## 3. Security Review

### General Security
- [ ] **Input validation** on all user inputs
- [ ] **No hardcoded secrets** or sensitive data
- [ ] **Parameterized queries** used (via Prisma)
- [ ] **Authentication checks** in place for protected operations
- [ ] **Authorization levels** appropriate for the operation
- [ ] **XSS prevention** in frontend (proper escaping)

### OWASP Compliance
- [ ] **Access control** follows least privilege principle
- [ ] **Cryptographic operations** use strong algorithms
- [ ] **No injection vulnerabilities** (SQL, command, etc.)
- [ ] **Secure configuration** (no debug info in production)
- [ ] **Session management** follows best practices
- [ ] **Data integrity** measures in place

## 4. Performance Considerations

### Backend Performance
- [ ] **Database queries optimized** (proper indexing considered)
- [ ] **N+1 query problems** avoided
- [ ] **Async operations** don't block unnecessarily
- [ ] **Memory usage** reasonable for operations
- [ ] **Response times** acceptable for user operations

### Frontend Performance
- [ ] **Bundle size impact** considered
- [ ] **Unnecessary re-renders** avoided
- [ ] **Lazy loading** implemented where appropriate
- [ ] **Images optimized** (using Next.js Image component)
- [ ] **API calls efficient** (proper caching, batching)

## 5. Testing & Quality Assurance

### Test Coverage
- [ ] **Unit tests** provided for new functionality
- [ ] **Integration tests** for API endpoints
- [ ] **E2E tests** for user-facing features (where applicable)
- [ ] **Edge cases** covered in tests
- [ ] **Error scenarios** tested

### Test Quality
- [ ] **Tests are deterministic** (no random failures)
- [ ] **Test names** clearly describe what is being tested
- [ ] **Mocks used appropriately** for external dependencies
- [ ] **Test data** is realistic and comprehensive
- [ ] **Cleanup** properly handled in tests

## 6. Documentation & Communication

### Code Documentation
- [ ] **Complex logic explained** with comments
- [ ] **API changes documented** (if applicable)
- [ ] **Breaking changes** clearly marked
- [ ] **Public interfaces** have proper JSDoc/docstrings
- [ ] **README updates** if functionality changes

### Change Documentation
- [ ] **PR description** clearly explains changes
- [ ] **Related issues** linked appropriately
- [ ] **Migration steps** documented (if needed)
- [ ] **Deployment considerations** noted

## 7. Compatibility & Integration

### System Integration
- [ ] **Backward compatibility** maintained (or breaking changes documented)
- [ ] **Database migrations** handled properly
- [ ] **API versioning** considered
- [ ] **Environment variables** usage documented
- [ ] **Dependencies** are necessary and up-to-date

### Browser/Platform Support
- [ ] **Cross-browser compatibility** considered
- [ ] **Mobile responsiveness** maintained
- [ ] **Accessibility standards** followed
- [ ] **Performance on slower devices** considered

## 8. Error Handling & Resilience

### Error Management
- [ ] **Graceful error handling** throughout
- [ ] **User-friendly error messages**
- [ ] **Proper error logging** for debugging
- [ ] **Fallback behavior** for failures
- [ ] **Resource cleanup** in error scenarios

### Monitoring & Observability
- [ ] **Appropriate logging** levels used
- [ ] **Metrics and monitoring** considerations
- [ ] **Debugging information** available
- [ ] **Performance monitoring** hooks in place

## Review Actions

### Approval Criteria
- [ ] All checklist items pass or have acceptable justification
- [ ] Tests pass in CI/CD pipeline
- [ ] No security vulnerabilities introduced
- [ ] Performance impact is acceptable
- [ ] Code follows AutoGPT standards and patterns

### Common Review Comments

#### Request Changes
```markdown
**Security Concern:** This endpoint lacks user authentication. Please add proper auth checks.

**Performance Issue:** This query could cause N+1 problems. Consider using includes/joins.

**Type Safety:** Missing type annotations for this function. Please add proper typing.

**Testing:** This new functionality needs unit tests. Please add test coverage.
```

#### Suggestions
```markdown
**Suggestion:** Consider using useMemo here to prevent unnecessary recalculations.

**Nit:** This could be simplified using the existing utility function in lib/utils.

**Enhancement:** Great implementation! Consider adding JSDoc for future maintainers.
```

## AutoGPT-Specific Review Points

### Backend Reviews
- [ ] **Prisma schema changes** include proper migrations
- [ ] **FastAPI routes** follow established patterns
- [ ] **Block system changes** maintain compatibility
- [ ] **Agent execution** handles errors gracefully
- [ ] **User data isolation** properly implemented

### Frontend Reviews
- [ ] **Next.js patterns** followed correctly
- [ ] **Tailwind classes** used appropriately
- [ ] **Component composition** follows established patterns
- [ ] **State management** uses React Query patterns
- [ ] **Error boundaries** handle failures properly

### Infrastructure Reviews
- [ ] **Docker configurations** follow best practices
- [ ] **CI/CD changes** don't break existing workflows
- [ ] **Environment configurations** are secure
- [ ] **Database changes** are reversible

## Final Review Decision

**Status:** ✅ Approved | ⚠️ Approved with Comments | ❌ Request Changes

**Summary:** Provide clear feedback on what was reviewed, any concerns, and next steps.

Conduct thorough reviews to maintain the high quality and security standards of the AutoGPT platform.