"""
Quick transcription example using dhvagna-npi.

This example demonstrates how to perform a simple speech-to-text transcription 
with minimal code using dhvagna-npi.
"""

import speech_recognition as sr
from dhvagna_npi.config import Config
from dhvagna_npi.core import transcribe_audio

def main():
    """Perform a quick transcription."""
    # Initialize recognizer and microphone
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    
    # Set a moderate sensitivity threshold
    recognizer.energy_threshold = 300
    
    print("=== Dhvagna-NPI Quick Transcription Example ===")
    print("Speak after the 'Listening...' message appears.")
    
    # Record and transcribe
    with microphone as source:
        print("\nAdjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        print("\nListening... Speak now!")
        audio = recognizer.listen(source, timeout=5)
        
        print("\nTranscribing...")
        success, text, error = transcribe_audio(audio, recognizer, "en-US")
        
        if success:
            print(f"\nTranscription: \"{text}\"")
        else:
            print(f"\nError: {error}")

if __name__ == "__main__":
    main()