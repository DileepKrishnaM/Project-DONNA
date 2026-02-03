# core/listener.py
import speech_recognition as sr

recognizer = sr.Recognizer()
recognizer.pause_threshold = 0.6

def listen(timeout=5):
    """
    Listens for speech with a timeout.
    Returns empty string if nothing is heard.
    """
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.3)
        print("[JARVIS] Listening...")
        try:
            audio = recognizer.listen(source, timeout=timeout)
        except sr.WaitTimeoutError:
            return ""

    try:
        return recognizer.recognize_google(audio).lower()
    except:
        return ""
