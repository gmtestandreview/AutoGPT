# GitHub Copilot Configuration Setup

## User Request
Follow instructions in github-copilot-starter.prompt.md to create comprehensive GitHub Copilot configuration for the AutoGPT repository.

## Project Analysis
- **Repository**: AutoGPT - AI agent platform monorepo
- **Primary Tech Stack**: Python/FastAPI backend, TypeScript/Next.js frontend
- **Languages**: Python 3.10-3.13, TypeScript, Next.js 15, React
- **Tools**: Docker, Poetry, pnpm, Playwright, Storybook
- **Architecture**: Large monorepo with autogpt_platform/ (main focus), classic/, docs/

## Action Plan

### Phase 1: Core Instructions Setup
- [ ] Update .github/copilot-instructions.md with comprehensive aggregated instructions
- [ ] Create language-specific instruction files (Python, TypeScript, Next.js, React)
- [ ] Integrate awesome-copilot patterns with proper attribution

### Phase 2: Prompts Creation  
- [ ] Create .github/prompts/ directory
- [ ] Add component setup prompts (setup-component.prompt.md, write-tests.prompt.md)
- [ ] Add development workflow prompts (code-review.prompt.md, debug-issue.prompt.md)
- [ ] Add architecture prompts (design-api.prompt.md, optimize-performance.prompt.md)

### Phase 3: Specialized Agents
- [ ] Create .github/agents/ directory
- [ ] Add role-based agents (architect.agent.md, reviewer.agent.md, debugger.agent.md)
- [ ] Add workflow-specific agents (testing.agent.md, security.agent.md)

### Phase 4: Workflow Integration
- [ ] Create .github/workflows/copilot-setup-steps.yml
- [ ] Configure for AutoGPT's Python/TypeScript stack
- [ ] Include setup validation and dependency checks

### Phase 5: Documentation & Guidelines
- [ ] Create README.md with usage instructions
- [ ] Add configuration guidelines
- [ ] Document customization options

## Current Status
- [x] Research awesome-copilot patterns complete
- [ ] Begin implementation following researched best practices