# main.py
import time
from core.listener import listen
from core.speaker import speak
from core.wake_word import is_wake_word
from core.brain import process

def start_donna():
    speak("Donna is online.")
    while True:
        # 1️⃣ Listen ONLY for wake word
        text = listen()
        if not text:
            continue

        print(f"[Heard]: {text}")

        if is_wake_word(text):
            print("[DONNA] Wake word detected")

            # 2️⃣ Speak response (NO listening here)
            speak("Yes?")
            time.sleep(0.6)

            # 3️⃣ Listen for command (separate phase)
            command = listen()
            if command:
                print(f"[Command]: {command}")
                process(command)

if __name__ == "__main__":
    start_donna()
