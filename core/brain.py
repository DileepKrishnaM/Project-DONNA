# core/brain.py
from core.speaker import speak
from commands.system import open_chrome, exit_donna
from commands.web import search_web

def process(command: str):
    if "open chrome" in command:
        speak("Opening Chrome")
        open_chrome()

    elif "search" in command:
        query = command.replace("search", "").strip()
        if query:
            speak(f"Searching for {query}")
            search_web(query)
        else:
            speak("What should I search for?")

    elif "exit" in command or "stop listening" in command:
        speak("Shutting down. Goodbye.")
        exit_donna()

    else:
        speak("I did not understand that command.")
