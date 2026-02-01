WAKE_WORDS = ["jarvis","donna"]

def is_wake_word(text : str) -> bool :
    text = text.lower().strip()
    return any(word in text for word in WAKE_WORDS)