# core/listener.py
import speech_recognition as sr

recognizer = sr.Recognizer()
recognizer.pause_threshold = 0.6

def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.3)
        print("[DONNA] Listening...")
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio).lower()
    except:
        return ""
