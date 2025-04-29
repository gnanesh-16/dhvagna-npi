# Testing Dhvagna-NPI

This document provides instructions for testing your Dhvagna-NPI package installation and functionality.

## Prerequisites

Before testing, make sure you have:

1. Installed the package (`pip install -e .` from the package root)
2. A working microphone connected to your computer
3. Permissions for the application to access your microphone

## Running the Unit Tests

The package includes unit tests to verify that the core components work correctly.

```bash
# Run all tests
python -m unittest discover -s tests

# Run specific test modules
python -m unittest tests.test_config
python -m unittest tests.test_history
python -m unittest tests.test_utils
```

## Testing the CLI

After installation, you should be able to run the command-line interfaces:

```bash
# Test quick mode
dhvagna-npi

# Test interactive mode
dhvagna-npi-interactive
```

## Testing with Example Scripts

The package includes several example scripts that demonstrate different features:

```bash
# Run the minimal example (just 9 lines)
python examples/minimal_example.py

# Test basic transcription
python examples/quick_transcribe.py

# Test custom settings
python examples/custom_settings.py

# Test saving to different file formats
python examples/save_to_file.py

# Test multilingual support
python examples/multilingual.py
```

## Manual Testing Checklist

1. **Basic Functionality**
   - [ ] Can record and transcribe speech
   - [ ] Displays transcription correctly
   - [ ] Can exit the application

2. **Settings**
   - [ ] Can access settings menu
   - [ ] Can change hotkey
   - [ ] Can change language
   - [ ] Can change save options
   - [ ] Can change timeout and sensitivity

3. **Multi-language Support**
   - [ ] Can transcribe in English
   - [ ] Can transcribe in at least one non-English language
   - [ ] Language selection works properly

4. **History**
   - [ ] Transcription history is stored correctly
   - [ ] Can view history
   - [ ] Files are saved to the correct location

## Troubleshooting

### Microphone Issues

If the application cannot detect your microphone:

1. Check that your microphone is properly connected
2. Verify that your operating system recognizes the microphone
3. Ensure the application has permission to access the microphone
4. Try adjusting the sensitivity settings

### Transcription Issues

If transcription quality is poor:

1. Speak clearly and at a moderate pace
2. Reduce background noise
3. Adjust the microphone sensitivity in settings
4. Try using a different language setting if speaking a different language

### Installation Issues

If you encounter problems with installation:

1. Ensure you have Python 3.7 or newer
2. Install the required dependencies manually:
   ```bash
   pip install SpeechRecognition keyboard rich
   ```
3. Check for error messages during installation and resolve any dependency issues

## Advanced Testing

For more advanced testing, you can:

1. Test with different microphone types
2. Test in noisy environments
3. Test with multiple speakers
4. Test recognition of specialized terminology