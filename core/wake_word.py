# core/wake_word.py

WAKE_KEYWORDS = ["friday", "jarvis", "hey jarvis", "okay jarvis", "alexa", "hey siri"]

def is_wake_word(text: str) -> bool:
    text = text.lower()
    return any(word in text for word in WAKE_KEYWORDS)
