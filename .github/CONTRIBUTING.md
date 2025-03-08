# Contributing to OIB Validator

Thank you for your interest in contributing to the OIB Validator project! This document provides guidelines and instructions for contributing.

## Code of Conduct

By participating in this project, you are expected to uphold our [Code of Conduct](CODE_OF_CONDUCT.md).

## How to Contribute

### Reporting Bugs

- Before submitting a bug report, please check existing issues to see if the problem has already been reported.
- Use the bug report template to create a new issue, providing as much detail as possible.
- Include steps to reproduce, expected behavior, actual behavior, and environment details.

### Suggesting Enhancements

- First, check that your idea isn't already in the works or previously rejected.
- Use the feature request template to create a new issue.
- Describe the enhancement in detail and explain why it would be valuable.

### Pull Requests

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Implement your changes
4. Add tests for your changes
5. Make sure all tests pass (`pytest`)
6. Update documentation as needed
7. Commit your changes (`git commit -m 'Add some amazing feature'`)
8. Push to the branch (`git push origin feature/amazing-feature`)
9. Open a Pull Request with a clear description of the changes

## Development Guidelines

### Code Style

- Follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
- Use [Google-style docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
- Include type hints for function parameters and return values

### Testing

- Add tests for new features or bug fixes
- Ensure all tests pass before submitting a PR
- Aim to maintain or improve code coverage

### Commit Messages

- Use clear and meaningful commit messages
- Reference issue numbers in commit messages when applicable

## Setting Up Development Environment

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/oib-validator.git
   cd oib-validator
   ```

2. Install development dependencies:

   ```
   pip install -e ".[dev]"
   ```

3. Run tests to make sure everything is working:

   ```
   pytest
   ```

## License

By contributing to this project, you agree that your contributions will be licensed under the project's [MIT License](../LICENSE).
