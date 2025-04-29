#!/usr/bin/env python
"""
Automation script for building and publishing the Dhvagna-NPI package to PyPI.
This script handles:
1. Cleaning previous builds
2. Running tests
3. Building distributions
4. Uploading to TestPyPI (optional)
5. Uploading to PyPI

Usage:
    python scripts/publish.py [--test] [--skip-tests] [--skip-clean]

Options:
    --test: Upload to TestPyPI instead of PyPI
    --skip-tests: Skip running tests
    --skip-clean: Skip cleaning previous builds
"""

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path


def run_command(command, description=None):
    """Run a shell command and print output."""
    if description:
        print(f"\n{description}...")
    
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    if result.stdout:
        print(result.stdout)
    
    if result.stderr:
        print(result.stderr)
    
    if result.returncode != 0:
        print(f"Error running command: {command}")
        sys.exit(1)
    
    return result


def clean_previous_builds():
    """Remove previous build directories."""
    print("\nCleaning previous builds...")
    
    # Define directories to remove
    directories = ["build", "dist", "src/dhvagna_npi.egg-info"]
    
    for directory in directories:
        if os.path.exists(directory):
            print(f"Removing {directory}")
            if os.path.isdir(directory):
                shutil.rmtree(directory)
            else:
                os.remove(directory)


def run_tests():
    """Run pytest with coverage."""
    run_command("pytest --cov=dhvagna_npi tests/", "Running tests with coverage")


def build_package():
    """Build source and wheel distributions."""
    run_command("python -m build", "Building package distributions")


def check_distributions():
    """Check distribution files with twine."""
    run_command("twine check dist/*", "Checking distribution files")


def upload_to_pypi(test=False):
    """Upload the package to PyPI or TestPyPI."""
    if test:
        run_command("twine upload --repository testpypi dist/*", 
                   "Uploading to TestPyPI")
        print("\n✅ Package uploaded to TestPyPI!")
        print("To install, run:")
        print("pip install --index-url https://test.pypi.org/simple/ dhvagna-npi")
    else:
        run_command("twine upload dist/*", 
                   "Uploading to PyPI")
        print("\n✅ Package uploaded to PyPI!")
        print("To install, run:")
        print("pip install dhvagna-npi")


def main():
    """Main function to handle the publication process."""
    parser = argparse.ArgumentParser(description="Build and publish the Dhvagna-NPI package")
    parser.add_argument("--test", action="store_true", help="Upload to TestPyPI instead of PyPI")
    parser.add_argument("--skip-tests", action="store_true", help="Skip running tests")
    parser.add_argument("--skip-clean", action="store_true", help="Skip cleaning previous builds")
    args = parser.parse_args()
    
    # Ensure we're in the project root directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(os.path.dirname(script_dir))
    
    # Print current directory and Python version
    print(f"Working directory: {os.getcwd()}")
    run_command("python --version", "Python version")
    
    # Run the publication steps
    if not args.skip_clean:
        clean_previous_builds()
    
    if not args.skip_tests:
        run_tests()
    
    build_package()
    check_distributions()
    upload_to_pypi(args.test)


if __name__ == "__main__":
    main()