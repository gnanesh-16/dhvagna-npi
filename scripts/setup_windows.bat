@echo off
echo ===================================
echo Dhvagna-NPI Development Environment Setup
echo ===================================
echo.

:: Check if Python is installed
where python >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo Python is not installed or not in PATH.
    echo Please install Python 3.7+ from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation.
    exit /b 1
)

:: Get Python version information
for /f "tokens=2" %%a in ('python --version 2^>^&1') do set PYTHON_VERSION=%%a
echo Python version: %PYTHON_VERSION%

:: Determine Python major and minor version
for /f "tokens=1,2 delims=." %%a in ("%PYTHON_VERSION%") do (
    set PYTHON_MAJOR=%%a
    set PYTHON_MINOR=%%b
)

:: Try to locate the actual Python executable
for /f "tokens=*" %%a in ('where python') do (
    set PYTHON_PATH=%%a
    goto :break_loop
)
:break_loop

echo Python executable: %PYTHON_PATH%

echo.
echo Creating virtual environment...
:: Force create a new virtual environment to ensure it works
if exist venv (
    echo Removing existing environment...
    rmdir /s /q venv
)

:: Try different methods to create the virtual environment
echo Method 1: Using direct venv module...
python -m venv venv

if not exist venv\Scripts\activate.bat (
    echo Method 1 failed. Trying Method 2: Using full path...
    "%PYTHON_PATH%" -m venv venv
)

if not exist venv\Scripts\activate.bat (
    echo Method 2 failed. Trying Method 3: Using virtualenv...
    pip install virtualenv
    python -m virtualenv venv
)

if not exist venv\Scripts\activate.bat (
    echo All methods failed to create a virtual environment.
    echo Please try creating it manually with:
    echo python -m venv venv
    exit /b 1
)

echo.
echo Virtual environment created successfully!
echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat

:: Verify activation
if "%VIRTUAL_ENV%"=="" (
    echo Failed to activate virtual environment!
    echo Please activate it manually: venv\Scripts\activate.bat
    exit /b 1
)

echo Virtual environment activated: %VIRTUAL_ENV%

echo.
echo Upgrading pip...
python -m pip install --upgrade pip

echo.
echo Installing development dependencies...
pip install -e .
pip install pytest pytest-cov black isort mypy build twine

echo.
echo Installing PyAudio dependency...
pip install pyaudio
if %ERRORLEVEL% neq 0 (
    echo PyAudio installation failed. Trying alternative method...
    pip install pipwin
    pipwin install pyaudio
    if %ERRORLEVEL% neq 0 (
        echo PyAudio installation failed with both methods.
        echo Downloading pre-built wheel...
        mkdir temp_wheels 2>nul
        echo Detecting Python version for wheel...
        
        :: Convert Python version for wheel filename format
        set PY_VER_NO_DOT=%PYTHON_MAJOR%%PYTHON_MINOR%
        
        :: Check architecture
        python -c "import platform; print('x64' if platform.architecture()[0] == '64bit' else 'x86')" > arch.txt
        set /p ARCH=<arch.txt
        del arch.txt
        echo Architecture: %ARCH%
        
        echo Attempting to download PyAudio wheel for Python %PYTHON_MAJOR%.%PYTHON_MINOR% %ARCH%...
        curl -L "https://download.lfd.uci.edu/pythonlibs/archived/PyAudio-0.2.11-cp%PY_VER_NO_DOT%-cp%PY_VER_NO_DOT%-win_%ARCH%.whl" -o temp_wheels\pyaudio.whl
        pip install temp_wheels\pyaudio.whl
        if %ERRORLEVEL% neq 0 (
            echo WARNING: Could not install PyAudio. Some functionality may not work.
            echo You may need to install PyAudio manually.
        ) else (
            echo PyAudio installed successfully from wheel!
        )
        rmdir /s /q temp_wheels
    )
)

echo.
echo Setting up pre-commit hooks...
pip install pre-commit

:: Create pre-commit config if it doesn't exist
if not exist .pre-commit-config.yaml (
    echo Creating .pre-commit-config.yaml...
    echo repos: > .pre-commit-config.yaml
    echo -   repo: https://github.com/pre-commit/pre-commit-hooks >> .pre-commit-config.yaml
    echo     rev: v4.4.0 >> .pre-commit-config.yaml
    echo     hooks: >> .pre-commit-config.yaml
    echo     -   id: trailing-whitespace >> .pre-commit-config.yaml
    echo     -   id: end-of-file-fixer >> .pre-commit-config.yaml
    echo     -   id: check-yaml >> .pre-commit-config.yaml
    echo     -   id: check-added-large-files >> .pre-commit-config.yaml
    echo. >> .pre-commit-config.yaml
    echo -   repo: https://github.com/psf/black >> .pre-commit-config.yaml
    echo     rev: 23.1.0 >> .pre-commit-config.yaml
    echo     hooks: >> .pre-commit-config.yaml
    echo     -   id: black >> .pre-commit-config.yaml
    echo. >> .pre-commit-config.yaml
    echo -   repo: https://github.com/pycqa/isort >> .pre-commit-config.yaml
    echo     rev: 5.12.0 >> .pre-commit-config.yaml
    echo     hooks: >> .pre-commit-config.yaml
    echo     -   id: isort >> .pre-commit-config.yaml
)

:: Initialize pre-commit
pre-commit install

echo.
echo Creating necessary directories if they don't exist...
if not exist src mkdir src
if not exist src\dhvagna_npi mkdir src\dhvagna_npi
if not exist tests mkdir tests
if not exist examples mkdir examples

:: Create empty __init__.py files if they don't exist
if not exist src\dhvagna_npi\__init__.py (
    echo Creating __init__.py...
    echo """Dhvagna-NPI - Advanced Voice Transcription Tool""" > src\dhvagna_npi\__init__.py
    echo. >> src\dhvagna_npi\__init__.py
    echo from .config import Config >> src\dhvagna_npi\__init__.py
    echo from .history import TranscriptionHistory >> src\dhvagna_npi\__init__.py
    echo from .core import main, run_interactive, run_single_transcription >> src\dhvagna_npi\__init__.py
    echo. >> src\dhvagna_npi\__init__.py
    echo __version__ = "0.1.0" >> src\dhvagna_npi\__init__.py
    echo __author__ = "dhvagna" >> src\dhvagna_npi\__init__.py
)

:: Fix tests/__init__.py if it exists
if exist tests\__init__.py (
    echo Fixing tests/__init__.py...
    echo """Test package for dhvagna-npi.""" > tests\__init__.py
    echo # Empty init file >> tests\__init__.py
) else (
    echo Creating tests/__init__.py...
    echo """Test package for dhvagna-npi.""" > tests\__init__.py
    echo # Empty init file >> tests\__init__.py
)

:: Update requirements.txt to include PyAudio
echo Updating requirements.txt to include PyAudio...
if not exist requirements.txt (
    echo Creating requirements.txt...
    echo SpeechRecognition>=3.8.0 > requirements.txt
    echo keyboard>=0.13.5 >> requirements.txt
    echo rich>=10.0.0 >> requirements.txt
    echo PyAudio>=0.2.11 >> requirements.txt
) else (
    findstr /i "PyAudio" requirements.txt >nul 2>&1
    if %ERRORLEVEL% neq 0 (
        echo PyAudio>=0.2.11 >> requirements.txt
    )
)

:: Fix pyproject.toml license format
if exist pyproject.toml (
    echo Fixing pyproject.toml license format...
    powershell -Command "(Get-Content pyproject.toml) -replace 'license = \{text = \"MIT\"\}', 'license = \"MIT\"' | Set-Content pyproject.toml"
    
    :: Add dynamic field for optional-dependencies
    powershell -Command "if (-not ((Get-Content pyproject.toml) -match 'dynamic')) { (Get-Content pyproject.toml) -replace '\[project\]', '[project]`r`ndynamic = [\"optional-dependencies\"]' | Set-Content pyproject.toml }"
)

:: Check for required files and fix __init__.py if needed
set missing_files=0
if not exist setup.py set missing_files=1
if not exist pyproject.toml set missing_files=1
if not exist src\dhvagna_npi\__init__.py set missing_files=1

if %missing_files% equ 1 (
    echo.
    echo WARNING: Some required files are missing.
    echo Please make sure you have all the necessary files for the package.
    echo Refer to DEVELOPER_README.md for the expected file structure.
)

echo.
echo Cleaning previous builds...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist src\dhvagna_npi.egg-info rmdir /s /q src\dhvagna_npi.egg-info

echo.
echo Building package...
python -m build

:: Check if build succeeded
if not exist dist (
    echo Build failed! Check the errors above.
    goto cleanup
)

echo.
echo Checking distribution package...
twine check dist/*

echo.
echo Testing package installation from wheel...
echo.
echo Creating test environment...
if exist test_venv rmdir /s /q test_venv
python -m venv test_venv
if %ERRORLEVEL% neq 0 (
    echo Failed to create test environment!
    goto cleanup
)

call test_venv\Scripts\activate.bat

echo Installing wheel package...
for %%f in (dist\*.whl) do (
    pip install %%f
    if %ERRORLEVEL% neq 0 (
        echo Failed to install wheel package!
        goto cleanup_test
    )
)

echo Installing PyAudio in test environment...
pip install pyaudio
if %ERRORLEVEL% neq 0 (
    echo PyAudio installation failed in test environment. Skipping audio tests.
) else (
    echo Testing package imports...
    python -c "import dhvagna_npi; print(f'Successfully imported dhvagna_npi version {dhvagna_npi.__version__}')"
    
    echo.
    echo Test CLI commands...
    where dhvagna-npi >nul 2>&1
    if %ERRORLEVEL% equ 0 (
        echo dhvagna-npi command is available!
    ) else (
        echo WARNING: dhvagna-npi command not found! Entry points may not be configured correctly.
    )
)

:cleanup_test
echo.
echo Deactivating test environment...
call test_venv\Scripts\deactivate.bat
echo Returning to development environment...
call venv\Scripts\activate.bat

echo.
echo Running unit tests...
pytest -xvs

:cleanup
echo.
echo ===================================
echo Development environment setup complete!
echo ===================================
echo.
echo Virtual environment: venv\Scripts\activate.bat
echo.
echo Package built successfully in dist/ directory
echo.
echo To test examples:
echo   python examples\minimal_example.py
echo.
echo To install package in a new environment:
for %%f in (dist\*.whl) do (
    echo   pip install "%%f"
)
echo.
echo To publish to PyPI:
echo   twine upload dist/*
echo.
echo To publish to TestPyPI:
echo   twine upload --repository testpypi dist/*
echo ===================================

echo.
echo Would you like to start working with the package now? (y/n)
set /p continue=

if /i "%continue%"=="y" (
    echo.
    echo Starting interactive session...
    echo Try running: python examples\minimal_example.py
    echo Or: python -m dhvagna_npi
    echo.
    cmd /k "venv\Scripts\activate.bat"
) else (
    echo.
    echo Setup completed. Exiting...
    exit /b 0
)