# core/brain.py
from core.speaker import speak
from core.intent import parse_intent
from commands.system import open_chrome, exit_donna
from commands.web import search_web

def process(command: str):
    intent, data = parse_intent(command)

    if intent == "open_app" and data == "chrome":
        speak("Opening Chrome")
        open_chrome()

    elif intent == "search_web":
        if data:
            speak(f"Searching for {data}")
            search_web(data)
        else:
            speak("What should I search for?")

    elif intent == "exit":
        speak("Shutting down. Goodbye.")
        exit_donna()

    else:
        speak("I did not understand that command.")
    