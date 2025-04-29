@echo off
echo Updating dhvagna-npi package...

:: Clean previous builds
if (Test-Path "build") { Remove-Item -Recurse -Force "build" }
if (Test-Path "dist") { Remove-Item -Recurse -Force "dist" }
if (Test-Path "src\dhvagna_npi.egg-info") { Remove-Item -Recurse -Force "src\dhvagna_npi.egg-info" }

:: Build new package
python -m build

:: Upload to PyPI
twine upload dist/*

echo Done!