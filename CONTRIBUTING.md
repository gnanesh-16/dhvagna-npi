# Contributing to dhvagna-npi

Thank you for your interest in contributing to **dhvagna-npi**, an advanced voice transcription tool with multi-language support! Contributions are welcome and appreciated. By contributing, you help make this project better, more robust, and accessible to all.

Please take a moment to review these contributing guidelines to ensure a smooth collaboration.

---

## Table of Contents

1. [How Can You Contribute?](#how-can-you-contribute)
2. [Code of Conduct](#code-of-conduct)
3. [Getting Started](#getting-started)
4. [Guidelines for Contributions](#guidelines-for-contributions)
    - [1. Reporting Issues](#1-reporting-issues)
    - [2. Proposing Enhancements](#2-proposing-enhancements)
    - [3. Submitting Code Contributions](#3-submitting-code-contributions)
5. [Development Setup](#development-setup)
6. [Coding Standards](#coding-standards)
7. [Testing](#testing)
8. [License](#license)

---

## How Can You Contribute?

You can contribute in the following ways:
- Reporting bugs or issues you encounter.
- Suggesting new features or enhancements.
- Writing or improving documentation.
- Submitting code contributions (fixing bugs, adding features, optimizing code, etc.).
- Writing tests to improve code coverage and robustness.

---

## Code of Conduct

This project adheres to the [Contributor Covenant Code of Conduct](./CODE_OF_CONDUCT.md). By participating, you agree to uphold this code. Instances of abusive, harassing, or otherwise unacceptable behavior may be reported to the maintainer at [gnanesh@example.com](mailto:gnanesh@example.com).

---

## Getting Started

1. **Fork the Repository**: Fork this repository to your GitHub account.
2. **Clone the Fork**: Clone your forked repository to your local machine.
    ```bash
    git clone [https://github.com/](https://github.com/)<your-username>/dhvagna-npi.git
    ```
3. **Set Upstream Remote**: Add the original repository as an upstream remote.
    ```bash
    git remote add upstream [https://github.com/gnanesh-16/dhvagna-npi.git](https://github.com/gnanesh-16/dhvagna-npi.git)
    ```
4. **Create a Branch**: Create a new branch for your contribution.
    ```bash
    git checkout -b feature/your-feature-name
    ```

---

## Guidelines for Contributions

### 1. Reporting Issues

- Search the [issue tracker](https://github.com/gnanesh-16/dhvagna-npi/issues) to ensure your issue hasn’t already been reported.
- If the issue doesn’t exist, open a [new issue](https://github.com/gnanesh-16/dhvagna-npi/issues/new).
- Provide as much detail as possible:
    - A clear, descriptive title.
    - Steps to reproduce the issue.
    - Expected vs. actual behavior.
    - Include any relevant logs, screenshots, or code snippets.

### 2. Proposing Enhancements

- Open a [discussion](https://github.com/gnanesh-16/dhvagna-npi/discussions) or an [issue](https://github.com/gnanesh-16/dhvagna-npi/issues/new) to propose changes before starting work.
- Clearly explain:
    - The need for the enhancement.
    - The proposed solution.
    - Any alternatives considered.

### 3. Submitting Code Contributions

- Follow the [Development Setup](#development-setup) guide to set up your local environment.
- Ensure your changes follow the [Coding Standards](#coding-standards) and pass all [tests](#testing).
- Commit your changes with clear, descriptive commit messages.
    ```bash
    git commit -m "Fix: Corrected issue with transcription alignment"
    ```
- Push your branch to your forked repository.
    ```bash
    git push origin feature/your-feature-name
    ```
- Open a [pull request (PR)](https://github.com/gnanesh-16/dhvagna-npi/pulls) to the `main` branch of the original repository.
- Provide a detailed description of your changes in the PR.
- Link any relevant issues or discussions in the PR.

---

## Development Setup

### 1. Prerequisites

- [Python](https://www.python.org/downloads/) 3.8 or higher.
- [pip](https://pip.pypa.io/en/stable/installing/) (Python package manager).
- [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) (recommended for managing dependencies).

### 2. Setting Up the Environment

- Create a virtual environment:
    ```bash
    python3 -m venv env
    ```
- Activate the virtual environment:
    - On Linux/macOS:
        ```bash
        source env/bin/activate
        ```
    - On Windows:
        ```bash
        .\env\Scripts\activate
        ```
- Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### 3. Running the Application

- To test the package locally, you can use:
    ```bash
    python main.py
    ```

---

## Coding Standards

### 1. Code Style

- Follow [PEP 8](https://peps.python.org/pep-0008/), the official Python style guide.
- Use tools like [flake8](https://flake8.pycqa.org/en/latest/) or [black](https://black.readthedocs.io/en/stable/) to check and format your code.
    ```bash
    pip install flake8 black
    flake8 .   # For linting
    black .    # For auto-formatting
    ```

### 2. Docstrings and Documentation

- Use [Google Style Python Docstrings](https://google.github.io/styleguide/pyguide.html#3_8_Documenting_Python) for documenting functions, classes, and modules.
- Keep comments concise and relevant.

---

## Testing

- Write tests for any new features or changes to existing functionality.
- Use the [pytest](https://docs.pytest.org/en/stable/) framework for testing.
    ```bash
    pip install pytest
    pytest
    ```
- Ensure all tests pass before submitting your pull request.

---

## License

This repository is licensed under a proprietary license specific to dhvagna-npi. Contributors must contact Gnanesh for permissions related to editing, reusing, or distributing this software.

Thank you for contributing to dhvagna-npi! Your support and efforts make this project better for everyone.
