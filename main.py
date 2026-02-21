# main.py
from core.listener import listen
from core.speaker import speak
from core.wake_word import is_wake_word
from core.brain import process
import threading
from commands.alarm import check_alarms
import time


def start_jarvis():
    speak("Jarvis is online.")

    # Start alarm background thread
    alarm_thread = threading.Thread(
        target=check_alarms,
        args=(speak,),
        daemon=True
    )
    alarm_thread.start()

    # Conversation state
    active_mode = False

    # Idle timeout settings
    IDLE_TIMEOUT = 20  # seconds
    last_active_time = time.time()

    while True:
        # IDLE MODE (Waiting for wake word)
        if not active_mode:
            text = listen(timeout=10)

            if not text:
                continue

            print(f"[Heard]: {text}")

            if is_wake_word(text):
                print("[JARVIS] Wake word detected")
                speak("Yes?")
                active_mode = True
                last_active_time = time.time()

            continue

        # ACTIVE MODE (Conversation Mode)

        # Auto sleep after inactivity
        if time.time() - last_active_time > IDLE_TIMEOUT:
            speak("Going back to sleep.")
            active_mode = False
            print("[JARVIS] Auto sleep triggered")
            continue

        # Listen for next command
        command = listen(timeout=8)

        # Silence → keep waiting until timeout
        if not command:
            continue

        print(f"[Command]: {command}")

        # Reset activity timer
        last_active_time = time.time()

        # Process command
        result = process(command)

        # Manual sleep command
        if result == "sleep":
            active_mode = False
            print("[JARVIS] Returning to idle")


if __name__ == "__main__":
    start_jarvis()