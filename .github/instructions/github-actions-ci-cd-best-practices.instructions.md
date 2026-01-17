# GitHub Actions CI/CD Best Practices

This file contains guidance for designing secure, efficient, and maintainable GitHub Actions workflows.

## Workflow Structure
- Use clear, modular workflows in `.github/workflows/*.yml` with descriptive names.
- Choose appropriate triggers: `push`, `pull_request`, `workflow_dispatch`, `schedule`, `workflow_call` for reusable workflows.
- Use `concurrency` to avoid duplicate runs and define `permissions` with least privilege.

## Jobs
- Represent distinct phases (build, test, lint, scan, deploy).
- Use `runs-on` appropriately (`ubuntu-latest`, `windows-latest`, `self-hosted`).
- Use `needs` to control job order and `outputs` to pass artifacts.
- Use `if` conditions for conditional execution.

## Security
- Manage secrets via GitHub Secrets; prefer OIDC for cloud authentication.
- Restrict `GITHUB_TOKEN` permissions to least privilege.

## Optimization
- Cache dependencies (`actions/cache`), use shallow clones (`fetch-depth`), and parallelize with `strategy.matrix`.

## Testing Strategy
- Run unit tests early, integration tests with services, and E2E in staged jobs; upload artifacts and test reports.

## Troubleshooting & Observability
- Upload test artifacts (JUnit, HTML) and use annotations for PR feedback.
- Use retention settings for artifacts and monitor workflow durations.

---

Use this file as a checklist when creating or reviewing GitHub Actions workflows.
