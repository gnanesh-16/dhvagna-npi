"""
Save transcription to file example using dhvagna-npi.

This example demonstrates how to save transcriptions to different file formats
including text, JSON, and CSV.
"""

import speech_recognition as sr
import json
import csv
import os
import datetime
from dhvagna_npi.config import Config
from dhvagna_npi.core import transcribe_audio
from dhvagna_npi.utils import get_language_name

def save_as_text(text, language, output_dir="output"):
    """Save transcription as a text file."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"transcription_{timestamp}.txt"
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"Timestamp: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Language: {get_language_name(language)}\n\n")
        f.write(text)
        
    return filepath

def save_as_json(text, language, output_dir="output"):
    """Save transcription as a JSON file."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"transcription_{timestamp}.json"
    filepath = os.path.join(output_dir, filename)
    
    data = {
        "timestamp": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "language": language,
        "language_name": get_language_name(language),
        "text": text
    }
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
        
    return filepath

def save_as_csv(text, language, output_dir="output"):
    """Save transcription as a CSV file."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"transcription_{timestamp}.csv"
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "Language", "Language Code", "Text"])
        writer.writerow([
            datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            get_language_name(language),
            language,
            text
        ])
        
    return filepath

def main():
    """Record speech and save transcription in multiple formats."""
    print("=== Dhvagna-NPI Save to File Example ===")
    
    # Initialize recognizer and microphone
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    language = "en-US"
    
    # Create output directory
    output_dir = "transcription_output"
    
    # Record and transcribe
    with microphone as source:
        print("\nAdjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        print("\nListening... Speak now!")
        audio = recognizer.listen(source)
        
        print("\nTranscribing...")
        success, text, error = transcribe_audio(audio, recognizer, language)
        
        if success:
            print(f"\nTranscription: \"{text}\"")
            
            # Save in different formats
            text_file = save_as_text(text, language, output_dir)
            json_file = save_as_json(text, language, output_dir)
            csv_file = save_as_csv(text, language, output_dir)
            
            print("\nSaved transcription to:")
            print(f"  - Text: {text_file}")
            print(f"  - JSON: {json_file}")
            print(f"  - CSV: {csv_file}")
        else:
            print(f"\nError: {error}")

if __name__ == "__main__":
    main()