# core/brain.py
from core.speaker import speak
from core.intent import parse_intent
from commands.system import open_chrome, exit_donna
from commands.web import search_web
from commands.whatsapp import send_whatsapp_message


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
    
    elif intent == "send_whatsapp":
        if data:
            phone_number = "+918309138662"
            speak("Sending WhatsApp message.")
            send_whatsapp_message(phone_number, data)
        else:
            speak("What message should I send?")
    
    else:
        speak("I did not understand that command.")
    