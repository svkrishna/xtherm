# Contributing to XTherm

Thank you for your interest in contributing to XTherm! This document provides guidelines and instructions for contributing to the project.

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/xtherm.git
   cd xtherm
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

## Code Style

We follow PEP 8 style guidelines with some additional requirements:

- Maximum line length: 88 characters (Black formatter)
- Use type hints for all function parameters and return values
- Document all public functions and classes with docstrings
- Use Google-style docstrings

### Formatting

We use the following tools for code formatting:

- Black for code formatting
- isort for import sorting
- flake8 for linting
- mypy for type checking

Run the formatting tools:
```bash
black .
isort .
flake8
mypy .
```

## Testing

### Running Tests

```bash
pytest
```

### Test Coverage

We maintain high test coverage. Run coverage report:
```bash
pytest --cov=xtherm tests/
```

### Writing Tests

- Place tests in the `tests/` directory
- Name test files `test_*.py`
- Use pytest fixtures for common setup
- Include both unit and integration tests
- Test edge cases and error conditions

Example test:
```python
def test_thermo_simulator_initialization():
    """Test ThermoSimulator initialization."""
    simulator = ThermoSimulator(
        grid_size=50,
        temperature=2.27,
        boundary=BoundaryCondition.PERIODIC
    )
    assert simulator.grid_size == 50
    assert simulator.temperature == 2.27
    assert simulator.boundary == BoundaryCondition.PERIODIC
```

## Documentation

### Building Documentation

```bash
cd docs
make html
```

### Documentation Guidelines

- Keep docstrings up to date
- Include examples in docstrings
- Document all parameters and return values
- Add new features to relevant documentation files
- Update API documentation when changing interfaces

## Performance Considerations

When adding new features:

1. Use Numba for performance-critical code:
   ```python
   @jit(nopython=True)
   def performance_critical_function():
       # Implementation
   ```

2. Consider parallel processing for large computations:
   ```python
   @jit(nopython=True, parallel=True)
   def parallel_function():
       # Implementation
   ```

3. Profile your code:
   ```bash
   python -m cProfile -o output.prof your_script.py
   ```

## Pull Request Process

1. Update documentation for new features
2. Add tests for new functionality
3. Ensure all tests pass
4. Update the changelog
5. Submit PR with clear description

## Commit Messages

Follow conventional commits format:
```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

Types:
- feat: New feature
- fix: Bug fix
- docs: Documentation changes
- style: Code style changes
- refactor: Code refactoring
- perf: Performance improvements
- test: Adding or modifying tests
- chore: Maintenance tasks

## Review Process

1. All PRs require at least one review
2. CI must pass
3. Code coverage must not decrease
4. Documentation must be updated
5. Performance impact must be considered

## Getting Help

- Open an issue for bugs
- Use discussions for questions
- Join our community chat
- Check existing documentation

## License

By contributing, you agree that your contributions will be licensed under the project's MIT License. 