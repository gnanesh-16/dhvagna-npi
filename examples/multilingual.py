"""
Multilingual transcription example using dhvagna-npi.

This example demonstrates how to transcribe speech in multiple languages
and how to switch between languages.
"""

import speech_recognition as sr
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box
from rich.prompt import Prompt

from dhvagna_npi.config import Config
from dhvagna_npi.core import transcribe_audio
from dhvagna_npi.utils import get_language_name, get_available_languages, get_language_codes

def display_language_table(console):
    """Display available languages in a table."""
    languages = get_available_languages()
    
    language_table = Table(title="Available Languages", box=box.ROUNDED)
    language_table.add_column("Option", style="cyan")
    language_table.add_column("Language", style="green")
    
    for key, value in languages.items():
        language_table.add_row(key, value)
    
    console.print(language_table)

def main():
    """Perform transcriptions in different languages."""
    console = Console()
    
    console.print(Panel(
        "Dhvagna-NPI Multilingual Example",
        style="bold magenta", 
        border_style="blue",
        box=box.DOUBLE
    ))
    
    # Display available languages
    display_language_table(console)
    
    # Get language choice
    lang_choice = Prompt.ask(
        "Select language", 
        choices=list(get_language_codes().keys()),
        default="1"
    )
    
    # Get the language code
    language_codes = get_language_codes()
    language = language_codes.get(lang_choice, "en-US")
    
    # Initialize recognizer and microphone
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    
    console.print(f"\nSelected language: [bold green]{get_language_name(language)}[/bold green]")
    console.print("Speak in the selected language after the prompt.")
    
    # Record and transcribe
    with microphone as source:
        console.print("\n[yellow]Adjusting for ambient noise...[/yellow]")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        console.print("\n[bold cyan]Listening... Speak now![/bold cyan]")
        audio = recognizer.listen(source)
        
        console.print("\n[yellow]Transcribing...[/yellow]")
        success, text, error = transcribe_audio(audio, recognizer, language)
        
        if success:
            console.print(Panel(
                text,
                title=f"[bold blue]Transcription in {get_language_name(language)}[/bold blue]",
                border_style="green",
                box=box.ROUNDED
            ))
            
            # If language is not English, try to recognize as English too for comparison
            if language != "en-US":
                try:
                    console.print("\n[yellow]Attempting English recognition of the same audio...[/yellow]")
                    english_text = recognizer.recognize_google(audio, language="en-US")
                    
                    console.print(Panel(
                        english_text,
                        title="[bold blue]Same Audio in English[/bold blue]",
                        border_style="yellow",
                        box=box.ROUNDED
                    ))
                except:
                    console.print("[red]Could not recognize speech in English.[/red]")
        else:
            console.print(f"\n[bold red]Error: {error}[/bold red]")
            
    # Ask if the user wants to try another language
    try_another = Prompt.ask(
        "\nWould you like to try another language?",
        choices=["y", "n"],
        default="n"
    )
    
    if try_another.lower() == "y":
        main()  # Restart the process

if __name__ == "__main__":
    main()