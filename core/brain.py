# core/brain.py
from core.speaker import speak
from core.intent import parse_intent
from commands.system import open_chrome, exit_donna
from commands.web import search_web
from commands.whatsapp import send_whatsapp_message
from core.contacts import get_contact_number

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
        if data and data.get("name") and data.get("message"):
            contact_name = data["name"]
            message = data["message"]

            phone_number = get_contact_number(contact_name)

            if phone_number:
                speak(f"Sending WhatsApp message to {contact_name}.")
                send_whatsapp_message(phone_number, message)
            else:
                speak(f"I do not have a contact named {contact_name}.")
        else:
            speak("Please tell me whom to message and what to say.")

    
    else:
        speak("I did not understand that command.")
    