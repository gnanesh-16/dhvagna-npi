"""
Minimal 9-line example using dhvagna-npi.

This example demonstrates how to perform speech-to-text transcription
with just 9 lines of code using dhvagna-npi.
"""

import speech_recognition as sr
from dhvagna_npi.core import transcribe_audio

# Initialize recognizer and microphone
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# Record and transcribe
with microphone as source:
    print("Listening... Speak now!")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)
    success, text, _ = transcribe_audio(audio, recognizer, "en-US")
    if success:
        print(f"Transcription: {text}")