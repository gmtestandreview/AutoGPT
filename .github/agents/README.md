# GitHub Copilot Agents

This directory contains specialized AI agents for different development tasks.

## Available Agents

- `architect.md` - Software architecture and system design specialist
- `reviewer.md` - Code review and quality assurance expert
- `debugger.md` - Bug tracking and issue resolution specialist

## Usage

Reference these agents in VS Code by typing `#file:.github/agents/[agent-name].md` in your Copilot chat to activate specialized behavior for specific tasks.

Example:
```
#file:.github/agents/architect.md

Design a new microservice for handling user authentication
```

## Agent Specializations

- **Architect**: System design, technology choices, scalability planning
- **Reviewer**: Code quality, security, performance optimization
- **Debugger**: Issue diagnosis, troubleshooting, root cause analysis