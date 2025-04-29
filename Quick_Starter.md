# Dhvagna-NPI Quick Start Guide for Developers

This guide provides the essential commands for quickly setting up, testing, and publishing the Dhvagna-NPI package.

## Initial Setup (Windows)

```cmd
:: Clone repository (if needed)
git clone https://github.com/dhvagna/dhvagna-npi.git
cd dhvagna-npi

:: Run the setup script
scripts\setup_windows.bat
```

## Manual Setup

```cmd
:: Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux

:: Install in development mode
pip install -e .
```

## Basic Testing

```cmd
:: Run all tests
pytest

:: Run with coverage
pytest --cov=dhvagna_npi tests/
```

## Building the Package

```cmd
:: Build source and wheel distributions
python -m build
```

## Testing Installation

```cmd
:: Test installation from wheel
scripts\test_install.bat

:: Or manually:
python -m venv test_venv
test_venv\Scripts\activate
pip install dist\dhvagna_npi-0.1.0-py3-none-any.whl
```

## Publishing to PyPI

```cmd
:: First, create .pypirc in your home directory
:: Use examples\.pypirc as a template

:: Upload to TestPyPI first
python scripts\publish.py --test

:: If successful, upload to PyPI
python scripts\publish.py
```

## Running the Application

```cmd
:: After installation
dhvagna-npi  # Quick mode
dhvagna-npi-interactive  # Interactive mode

:: In development
python -m dhvagna_npi.core  # Quick mode
python -m dhvagna_npi.core run_interactive  # Interactive mode
```

## Common Issues

1. **Microphone not working**:
   - Ensure microphone permissions are enabled
   - Try adjusting energy threshold: `recognizer.energy_threshold = 300`

2. **Package not found after installation**:
   - Verify entry points in setup.py
   - Check if installation was successful: `pip list | findstr dhvagna`

3. **PyPI upload errors**:
   - Verify your token is correct in .pypirc
   - Check if package name is available on PyPI
   - Ensure version number has been incremented

## Essential Files to Check

- `src/dhvagna_npi/__init__.py`: Version and package imports
- `setup.py`: Package metadata and entry points
- `pyproject.toml`: Build configuration