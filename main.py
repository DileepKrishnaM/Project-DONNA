# main.py
from core.listener import listen
from core.speaker import speak
from core.wake_word import is_wake_word
from core.brain import process

def start_jarvis():
    speak("Jarvis is online.")

    while True:
        # Idle mode: listen only for wake word
        text = listen(timeout=10)
        if not text:
            continue

        print(f"[Heard]: {text}")

        if is_wake_word(text):
            print("[JARVIS] Wake word detected")
            speak("Yes?")

            # Command mode: listen ONCE for command
            command = listen(timeout=6)

            if command:
                print(f"[Command]: {command}")
                process(command)
            else:
                speak("I did not hear any command.")

            print("[JARVIS] Returning to idle")

if __name__ == "__main__":
    start_jarvis()
