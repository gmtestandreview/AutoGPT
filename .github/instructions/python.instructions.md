---
description: 'Python coding conventions and best practices for AutoGPT development'
applyTo: '**/*.py'
---

# Python Development Standards

<!-- Based on: https://github.com/github/awesome-copilot/main/instructions/python.instructions.md -->

## Code Quality & Style

- **Write clear and concise comments** for each function and complex logic
- **Use descriptive names** for functions, variables, and classes
- **Include type hints** from the `typing` module (e.g., `List[str]`, `Dict[str, int]`)
- **Provide docstrings** following PEP 257 conventions for all functions and classes
- **Break down complex functions** into smaller, more manageable functions
- **Follow PEP 8** style guide for Python code formatting

## Code Style and Formatting

- **Maintain proper indentation** using 4 spaces for each level
- **Keep lines under 79 characters** for better readability
- **Place docstrings immediately** after the `def` or `class` keyword
- **Use blank lines** to separate functions, classes, and logical code blocks
- **Run `poetry run format`** before committing (Black + isort formatting)
- **Run `poetry run lint`** after formatting to catch style issues

## Type Safety & Documentation

- **Enable strict mode** in type checking tools where available
- **Use type annotations** for function parameters and return types
- **Document edge cases** and expected behavior in docstrings
- **Include examples** in docstrings for complex functions

## Testing & Quality Assurance

- **Write unit tests** for critical paths and all public functions
- **Include test cases** for edge cases like empty inputs, invalid data types, and large datasets
- **Document test cases** with descriptive names and docstrings
- **Use `poetry run test`** to run the full test suite
- **Use `poetry run pytest path/to/test.py`** for specific tests

## AutoGPT-Specific Patterns

- **Use async/await** for I/O-bound operations in the FastAPI backend
- **Implement proper error handling** with structured exceptions
- **Use Prisma ORM patterns** for database interactions
- **Follow the block system architecture** for agent execution blocks
- **Validate user ID checks** for any `data/*.py` changes for security

## Example of Proper Documentation

```python
def calculate_area(radius: float) -> float:
    """
    Calculate the area of a circle given the radius.
    
    Parameters:
    radius (float): The radius of the circle.
    
    Returns:
    float: The area of the circle, calculated as π * radius^2.
    
    Raises:
    ValueError: If radius is negative.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    
    import math
    return math.pi * radius ** 2
```

## Security Considerations

- **Validate all inputs** from external sources
- **Use parameterized queries** with Prisma ORM
- **Never hardcode secrets**; use environment variables
- **Sanitize file paths** to prevent directory traversal
- **Implement proper authentication checks** in API endpoints

---

Use this file when creating or reviewing Python code and tests.
