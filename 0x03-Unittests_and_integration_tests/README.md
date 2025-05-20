# 0x03-Unittests_and_integration_tests

This project contains unit and integration tests for Python modules, following best practices for testing with `unittest`, `parameterized`, and `mock`.

## Structure
- `test_utils.py`: Unit tests for utility functions.
- `test_client.py`: Unit and integration tests for the GithubOrgClient class.
- `utils.py`: Utility functions to be tested.
- `client.py`: Client code for interacting with GitHub API.
- `fixtures.py`: Fixtures for integration tests.

## Requirements
- Python 3.7
- All files are executable and follow pycodestyle (2.5)
- Each module, class, and function is documented

## How to run tests
```bash
python3 -m unittest discover 0x03-Unittests_and_integration_tests
```
