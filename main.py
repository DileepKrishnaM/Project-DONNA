# main.py
from core.listener import listen
from core.speaker import speak
from core.wake_word import is_wake_word
from core.brain import process
import threading
from commands.alarm import check_alarms


def start_jarvis():
    speak("Jarvis is online.")

    # Start alarm background thread
    alarm_thread = threading.Thread(
        target=check_alarms,
        args=(speak,),
        daemon=True
    )
    alarm_thread.start()

    active_mode = False  # conversation state

    while True:

        # IDLE MODE (Wake Word)
        if not active_mode:
            text = listen(timeout=10)

            if not text:
                continue

            print(f"[Heard]: {text}")

            if is_wake_word(text):
                print("[JARVIS] Wake word detected")
                speak("Yes?")
                active_mode = True

            continue

        # ACTIVE MODE (Multiple Commands)
        command = listen(timeout=8)

        # If silence → go back to idle
        if not command:
            speak("Going back to sleep.")
            active_mode = False
            print("[JARVIS] Returning to idle")
            continue

        print(f"[Command]: {command}")

        result = process(command)

        # stop listening command
        if result == "sleep":
            active_mode = False
            print("[JARVIS] Returning to idle")


if __name__ == "__main__":
    start_jarvis()
