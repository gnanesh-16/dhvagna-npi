"""
Custom settings example using dhvagna-npi.

This example demonstrates how to customize the configuration settings
for dhvagna-npi and use them for transcription.
"""

import speech_recognition as sr
from dhvagna_npi.config import Config
from dhvagna_npi.core import transcribe_audio
from dhvagna_npi.utils import get_language_name
import os

def main():
    """Perform transcription with custom settings."""
    # Create a custom config
    config = Config()
    
    # Customize settings
    # config.language = "es-ES"  # Spanish
    config.language = "en-US"  # English (US)
    config.energy_threshold = 250  # More sensitive
    config.timeout = 10  # 10 second timeout
    

    config.save_transcriptions = True
    
    # Create a custom transcription folder in the current directory
    custom_folder = os.path.join(os.getcwd(), "my_transcriptions")
    config.transcription_folder = custom_folder
    if not os.path.exists(custom_folder):
        os.makedirs(custom_folder)
    
    # Initialize recognizer with custom settings
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = config.energy_threshold
    recognizer.dynamic_energy_threshold = True
    recognizer.pause_threshold = 0.8
    
    microphone = sr.Microphone()
    
    print("=== Dhvagna-NPI Custom Settings Example ===")
    print(f"Language: {get_language_name(config.language)}")
    print(f"Microphone Sensitivity: {config.energy_threshold}")
    print(f"Timeout: {config.timeout} seconds")
    print(f"Transcriptions will be saved to: {config.transcription_folder}")
    
    # Record and transcribe
    with microphone as source:
        print("\nAdjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        print("\nListening... Speak now!")
        try:
            audio = recognizer.listen(source, timeout=config.timeout)
            
            print("\nTranscribing...")
            success, text, error = transcribe_audio(audio, recognizer, config.language)
            
            if success:
                print(f"\nTranscription ({get_language_name(config.language)}): \"{text}\"")
                
                # Save transcription if enabled
                if config.save_transcriptions:
                    timestamp = "example_transcription"
                    filename = f"transcription_{timestamp}.txt"
                    filepath = os.path.join(config.transcription_folder, filename)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(f"Language: {get_language_name(config.language)}\n\n{text}")
                    print(f"\nTranscription saved to: {filepath}")
            else:
                print(f"\nError: {error}")
                
        except sr.WaitTimeoutError:
            print("\nNo speech detected within the timeout period.")

if __name__ == "__main__":
    main()