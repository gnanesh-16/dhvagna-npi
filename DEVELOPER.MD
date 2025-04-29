# Dhvagna-NPI Developer Guide

This developer guide provides comprehensive instructions for setting up the development environment, building, testing, and publishing the Dhvagna-NPI package to PyPI. The guide focuses on Windows development but includes notes for other platforms.

## Table of Contents

1. [Development Environment Setup](#development-environment-setup)
2. [Installing Development Dependencies](#installing-development-dependencies)
3. [Package Structure](#package-structure)
4. [Building the Package](#building-the-package)
5. [Testing the Package](#testing-the-package)
6. [Publishing to PyPI](#publishing-to-pypi)
7. [Creating a PyPI Organization](#creating-a-pypi-organization)
8. [Continuous Integration](#continuous-integration)
9. [Version Management](#version-management)
10. [Troubleshooting](#troubleshooting)

## Development Environment Setup

### Windows Setup

1. **Install Python 3.7 or higher**
   - Download from [python.org](https://www.python.org/downloads/)
   - Ensure you check "Add Python to PATH" during installation

2. **Create and activate a virtual environment**
   ```cmd
   :: Navigate to your project directory
   cd path\to\dhvagna-npi

   :: Create a virtual environment
   python -m venv venv

   :: Activate the virtual environment
   venv\Scripts\activate
   ```

3. **Verify Python version**
   ```cmd
   python --version
   ```

### Alternative: Using Conda (Optional)

```cmd
:: Create a conda environment
conda create -n dhvagna-env python=3.9

:: Activate the environment
conda activate dhvagna-env
```

## Installing Development Dependencies

```cmd
:: With the virtual environment activated, install development dependencies
pip install -e .[dev]

:: If the above doesn't work, install these packages manually
pip install -e .
pip install pytest pytest-cov black isort mypy build twine
```

To make this work, update your `setup.py` with these extras_require:

```python
extras_require={
    'dev': [
        'pytest>=7.0.0',
        'pytest-cov>=3.0.0',
        'black>=22.0.0',
        'isort>=5.10.0',
        'mypy>=0.950',
        'build>=0.8.0',
        'twine>=4.0.0',
    ],
}
```

# Dhvagna-NPI Complete Package Structure

```
dhvagna-npi/
├── src/
│   └── dhvagna_npi/
│       ├── __init__.py                 # Package initialization, version and imports
│       ├── core.py                     # Main functionality for recording/transcription
│       ├── config.py                   # Configuration management
│       ├── history.py                  # Transcription history management
│       ├── ui.py                       # User interface components
│       ├── utils.py                    # Utility functions
│       └── cli.py                      # Command-line interface
├── tests/
│   ├── __init__.py
│   ├── test_config.py                  # Tests for config module
│   ├── test_history.py                 # Tests for history module
│   └── test_utils.py                   # Tests for utils module
├── examples/
│   ├── minimal_example.py              # Super simple 9-line implementation
│   ├── quick_transcribe.py             # Basic transcription example
│   ├── custom_settings.py              # Demonstrates customizing settings
│   ├── save_to_file.py                 # Shows saving to various file formats
│   ├── multilingual.py                 # Demonstrates multi-language support
│   └── .pypirc                         # Template for PyPI authentication
├── scripts/
│   ├── setup_windows.bat               # Windows setup automation
│   ├── test_install.bat                # Installation testing script
│   └── publish.py                      # Package publishing automation
├── .github/
│   └── workflows/
│       └── python-package.yml          # GitHub Actions workflow configuration
├── setup.py                            # Package installation script
├── pyproject.toml                      # Modern build configuration
├── README.md                           # User documentation
├── DEVELOPER_README.md                 # Developer documentation
├── QUICK_START.md                      # Quick reference for common tasks
├── TESTING.md                          # Testing guide
├── LICENSE                             # MIT License
├── requirements.txt                    # Dependencies
├── .gitignore                          # Git ignore patterns
└── MANIFEST.in                         # Additional files to include
```

## Building the Package

### Development Installation

```cmd
:: Install in development mode
pip install -e .

:: Verify installation
python -c "import dhvagna_npi; print(dhvagna_npi.__version__)"
```

### Building Distribution Packages

```cmd
:: Install build tools if not already installed
pip install build

:: Build source distribution and wheel
python -m build

:: This will create a dist/ directory with:
:: - dhvagna_npi-0.1.0.tar.gz (source distribution)
:: - dhvagna_npi-0.1.0-py3-none-any.whl (wheel distribution)
```

## Testing the Package

### Running Automated Tests

```cmd
:: Install pytest if not already installed
pip install pytest pytest-cov

:: Run all tests
pytest

:: Run tests with coverage report
pytest --cov=dhvagna_npi tests/

:: Generate coverage HTML report
pytest --cov=dhvagna_npi --cov-report=html tests/
```

### Testing the Package CLI

After installation, verify the CLI commands work:

```cmd
:: Test quick mode
dhvagna-npi

:: Test interactive mode
dhvagna-npi-interactive
```

### Testing the Package with Examples

```cmd
:: Run the minimal example
python examples/minimal_example.py

:: Run other examples
python examples/quick_transcribe.py
python examples/multilingual.py
```

### Testing Installation from Distribution Files

```cmd
:: Create a fresh virtual environment for testing
python -m venv test_venv
test_venv\Scripts\activate

:: Install from the wheel file
pip install dist\dhvagna_npi-0.1.0-py3-none-any.whl

:: Test basic functionality
dhvagna-npi --version
```

## Publishing to PyPI

### Setting Up PyPI Account

1. Register for a PyPI account at [PyPI](https://pypi.org/account/register/)
2. Set up API tokens for secure uploading

### Creating and Configuring .pypirc File

Create a file named `.pypirc` in your home directory (`C:\Users\YourUsername\`):

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
repository = https://upload.pypi.org/legacy/
username = __token__
password = pypi-YOUR-TOKEN-HERE

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-YOUR-TEST-TOKEN-HERE
```

### Testing Upload with TestPyPI

```cmd
:: Install twine if not already installed
pip install twine

:: Check distribution files
twine check dist/*

:: Upload to TestPyPI
twine upload --repository testpypi dist/*

:: Install from TestPyPI to verify
pip install --index-url https://test.pypi.org/simple/ dhvagna-npi
```

### Publishing to PyPI

```cmd
:: Upload to PyPI
twine upload dist/*

:: Or with username/password if not using .pypirc
twine upload -u __token__ -p your-token-here dist/*
```

## Creating a PyPI Organization

If you want to publish under an organization namespace:

1. **Create a PyPI account** if you don't have one

2. **Create an organization**:
   - Navigate to https://pypi.org/manage/organizations/
   - Click "Create new organization"
   - Enter organization name, display name, and other details
   - Add team members if necessary

3. **Upload package with organization namespace**:
   - Ensure your package name in `setup.py` and `pyproject.toml` follows the pattern:
     ```
     name = "dhvagna-org-name.dhvagna-npi"
     ```
   - Upload normally to PyPI with twine

4. **Transfer ownership**:
   - If the package already exists, go to the package page
   - Click "Manage" tab
   - Click "Transfer ownership"
   - Select the organization as the new owner

## Continuous Integration

### Setting Up GitHub Actions

Create a file at `.github/workflows/python-package.yml`:

```yaml
name: Python Package

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [windows-latest, ubuntu-latest, macos-latest]
        python-version: [3.7, 3.8, 3.9, '3.10']

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v2
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        python -m pip install pytest
        pip install -e .
    - name: Test with pytest
      run: |
        pytest
```

## Version Management

### Updating Version Numbers

1. Update version in these files:
   - `src/dhvagna_npi/__init__.py`
   - `setup.py`
   - `pyproject.toml`

2. Create a Git tag for the release:
   ```cmd
   git tag -a v0.1.0 -m "Version 0.1.0"
   git push origin v0.1.0
   ```

## Advanced Configuration

### Creating Entry Points

In your `setup.py`, ensure you have:

```python
entry_points={
    'console_scripts': [
        'dhvagna-npi=dhvagna_npi.core:main',
        'dhvagna-npi-interactive=dhvagna_npi.core:run_interactive',
    ],
},
```

### Setting up code formatting with pre-commit

1. Install pre-commit:
   ```cmd
   pip install pre-commit
   ```

2. Create `.pre-commit-config.yaml`:
   ```yaml
   repos:
   -   repo: https://github.com/pre-commit/pre-commit-hooks
       rev: v4.4.0
       hooks:
       -   id: trailing-whitespace
       -   id: end-of-file-fixer
       -   id: check-yaml
       -   id: check-added-large-files

   -   repo: https://github.com/psf/black
       rev: 23.1.0
       hooks:
       -   id: black

   -   repo: https://github.com/pycqa/isort
       rev: 5.12.0
       hooks:
       -   id: isort
   ```

3. Initialize pre-commit:
   ```cmd
   pre-commit install
   ```

## Troubleshooting

### Common Windows Issues

1. **Path Too Long Errors**:
   - Set Git to handle long paths:
     ```cmd
     git config --system core.longpaths true
     ```
   - Use shorter paths where possible

2. **Permission Issues**:
   - Run Command Prompt as Administrator
   - Ensure you have write permissions to the installation directories

3. **Dependencies Issues**:
   - If you encounter "Microsoft Visual C++ Build Tools" errors:
     Download and install from: https://visualstudio.microsoft.com/visual-cpp-build-tools/

4. **PyPI Upload Issues**:
   - Check your token permissions
   - Ensure your package name is unique on PyPI
   - Verify your `.pypirc` file is correctly formatted
   - Check internet connection and firewall settings

### Package Install Verification

To verify your package is correctly installed and working:

```cmd
:: Generate a basic transcript
python -c "from dhvagna_npi.core import main; main()"
```

## Complete Build and Publish Workflow

Here's a complete workflow for building and publishing your package:

```cmd
:: Activate your virtual environment
venv\Scripts\activate

:: Clean previous builds
rmdir /s /q build dist *.egg-info

:: Run tests
pytest

:: Build package
python -m build

:: Check distribution packages
twine check dist/*

:: Upload to TestPyPI first
twine upload --repository testpypi dist/*

:: Test installation from TestPyPI
pip install --index-url https://test.pypi.org/simple/ dhvagna-npi

:: If everything works, upload to real PyPI
twine upload dist/*
```

---

This guide covers all the essential steps for developing, building, testing, and publishing the Dhvagna-NPI package. For additional help, refer to the [Python Packaging User Guide](https://packaging.python.org/).