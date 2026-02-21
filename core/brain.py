# core/brain.py
from core.speaker import speak
from core.intent import parse_intent
from commands.system import (
    open_application,
    close_application,
    exit_donna,
    shutdown_computer,
    restart_computer,
    cancel_shutdown
)
from commands.web import search_web
from commands.whatsapp import send_whatsapp_message
from core.contacts import get_contact_number
from commands.media import play_song
from commands.system_info import get_time, get_date, get_battery
from commands.reminder import add_reminder, get_reminders
from commands.alarm import add_alarm, clear_alarms
from commands.volume import increase_volume, decrease_volume, mute_volume
from commands.knowledge import get_summary

# Confirmation Memory
pending_action = None

def process(command: str):
    global pending_action

    intent, data = parse_intent(command)
    command_lower = command.lower().strip()

    # CONFIRMATION RESPONSE
    if pending_action:

        if any(word in command_lower for word in ["yes", "confirm", "do it", "sure", "okay"]):
            action = pending_action
            pending_action = None
            action()
            return

        elif any(word in command_lower for word in ["no", "cancel", "stop"]):
            pending_action = None
            speak("Cancelled.")
            return

        else:
            speak("Please say yes or no.")
            return

    # ---- OPEN APPLICATION ----
    if intent == "open_app":
        if data:
            success = open_application(data)
            if success:
                speak(f"Opening {data}")
            else:
                speak("I couldn't open that application.")

    # ---- CLOSE APPLICATION (CONFIRMATION) ----
    elif intent == "close_app":

        def action():
            success = close_application(data)
            if success:
                speak(f"Closing {data}")
            else:
                speak("I could not close that application.")

        speak(f"Are you sure you want to close {data}?")
        pending_action = action
        return

    # ---- SEARCH WEB ----
    elif intent == "search_web":
        if data:
            speak(f"Searching for {data}")
            search_web(data)
        else:
            speak("What should I search for?")

    # ---- PLAY MUSIC ----
    elif intent == "play_music":
        speak(f"Playing {data}")
        play_song(data)

    # ---- VOLUME CONTROL ----
    elif intent == "volume_up":
        speak("Increasing volume.")
        increase_volume()

    elif intent == "volume_down":
        speak("Decreasing volume.")
        decrease_volume()

    elif intent == "volume_mute":
        speak("Muting volume.")
        mute_volume()

    # ---- WHATSAPP ----
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

    # ---- SYSTEM INFO ----
    elif intent == "get_time":
        speak(f"The time is {get_time()}")

    elif intent == "get_date":
        speak(f"Today is {get_date()}")

    elif intent == "get_battery":
        speak(get_battery())

    # ---- REMINDERS ----
    elif intent == "add_reminder":
        if data:
            add_reminder(data)
            speak("Reminder saved.")
        else:
            speak("What should I remind you about?")

    elif intent == "list_reminders":
        reminders = get_reminders()
        if reminders:
            speak("Here are your reminders.")
            for r in reminders[:5]:
                speak(r)
        else:
            speak("You have no reminders.")

    # ---- ALARMS ----
    elif intent == "set_alarm":
        if data:
            add_alarm(data)
            speak(f"Alarm set for {data}")
        else:
            speak("Please tell me the alarm time.")

    elif intent == "clear_alarms":
        clear_alarms()
        speak("All alarms have been cleared.")

    # ---- SHUTDOWN (CONFIRMATION) ----
    elif intent == "shutdown":
        speak("Are you sure you want to shut down?")
        pending_action = shutdown_computer
        return

    # ---- RESTART (CONFIRMATION) ----
    elif intent == "restart":
        speak("Are you sure you want to restart?")
        pending_action = restart_computer
        return

    elif intent == "cancel_shutdown":
        cancel_shutdown()
        speak("Shutdown cancelled.")

    # ---- HELP ----
    elif intent == "help":
        speak(
            "I can open and close applications, search the web, play music, "
            "send WhatsApp messages, set reminders and alarms, control volume, "
            "and provide system information like time, date, and battery."
        )

    # ---- KNOWLEDGE ----
    elif intent == "knowledge":
        if data:
            speak("Let me check.")
            answer = get_summary(data)
            speak(answer)
        else:
            speak("What would you like to know?")

    # ---- STOP LISTENING ----
    elif intent == "stop_listening":
        speak("Going back to sleep.")
        return "sleep"

    # ---- EXIT PROGRAM ----
    elif intent == "exit":
        speak("Shutting down. Goodbye.")
        exit_donna()

    else:
        speak("I did not understand that command.")