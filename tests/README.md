# Tests Directory

This directory contains the test suite for the Survey Data Filtering Dashboard.

## Structure

- `unit/` - Unit tests for individual functions and components
- `integration/` - Integration tests for complete workflows
- `conftest.py` - Pytest configuration and fixtures
- `test_requirements.txt` - Testing-specific dependencies

## Test Categories

### Unit Tests (`unit/`)
- Data loading and processing functions
- Filtering logic
- Chart generation
- Utility functions
- Configuration handling

### Integration Tests (`integration/`)
- End-to-end application workflows
- File upload and processing
- User interface interactions
- Data export functionality
- Performance benchmarks

## Running Tests

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test category
pytest tests/unit/
pytest tests/integration/

# Run with verbose output
pytest -v

# Run parallel tests
pytest -n auto
```

## Test Configuration

Tests use the following frameworks and tools:
- **pytest** - Main testing framework
- **pytest-cov** - Coverage reporting
- **pytest-mock** - Mocking support
- **pytest-xdist** - Parallel test execution

## Coverage Goals

- Minimum code coverage: 85%
- Critical functions: 95%
- New features: 100%

## Test Data

Test data files are stored in `tests/data/` and include:
- Sample CSV files for testing
- Edge case datasets
- Performance testing files

## Continuous Integration

Tests are automatically run on:
- Every push to main/develop branches
- All pull requests
- Nightly builds
- Before releases

## Writing Tests

Follow these guidelines when writing tests:
- Use descriptive test names
- Include docstrings for complex tests
- Mock external dependencies
- Test both success and failure scenarios
- Keep tests isolated and independent
