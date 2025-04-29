@echo off
echo ===================================
echo Dhvagna-NPI Installation Test Script
echo ===================================
echo.
echo This script will create a new virtual environment and 
echo install the package from the distribution files to 
echo ensure everything works correctly.
echo.

:: Ask for confirmation
set /p continue="Continue? (y/n): "
if /i not "%continue%"=="y" (
    echo Aborted.
    exit /b 0
)

:: Create a test directory
set test_dir=test_install
if not exist %test_dir% mkdir %test_dir%
cd %test_dir%

echo.
echo Creating test virtual environment...
python -m venv test_venv

echo.
echo Activating test environment...
call test_venv\Scripts\activate.bat

echo.
echo Upgrading pip...
python -m pip install --upgrade pip

:: Check if wheel exists
if not exist ..\dist\*.whl (
    echo.
    echo No wheel distribution found in dist/ directory.
    echo Please build the package first with: python -m build
    goto cleanup
)

echo.
echo Installing from wheel distribution...
pip install ..\dist\dhvagna_npi-0.1.0-py3-none-any.whl

echo.
echo Verifying installation...
python -c "import dhvagna_npi; print(f'dhvagna-npi version {dhvagna_npi.__version__} installed successfully!')"

echo.
echo Testing CLI commands...
where dhvagna-npi >nul 2>nul
if %ERRORLEVEL% equ 0 (
    echo dhvagna-npi command found!
) else (
    echo WARNING: dhvagna-npi command not found! Check entry points configuration.
)

where dhvagna-npi-interactive >nul 2>nul
if %ERRORLEVEL% equ 0 (
    echo dhvagna-npi-interactive command found!
) else (
    echo WARNING: dhvagna-npi-interactive command not found! Check entry points configuration.
)

echo.
echo ===================================
echo Installation test complete!
echo ===================================

:cleanup
echo.
echo Cleaning up...
cd ..
echo Deactivating test environment...
call %test_dir%\test_venv\Scripts\deactivate.bat

echo.
set /p remove="Remove test directory? (y/n): "
if /i "%remove%"=="y" (
    echo Removing test directory...
    rmdir /s /q %test_dir%
    echo Test directory removed.
) else (
    echo Test directory kept at: %CD%\%test_dir%
)

echo.
echo Done!