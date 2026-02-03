# core/intent.py

def parse_intent(command: str):
    command = command.lower()

    if any(word in command for word in ["open", "launch", "start"]):
        if "chrome" in command:
            return ("open_app", "chrome")

    if any(word in command for word in ["search", "google", "find"]):
        query = command.replace("search", "").replace("google", "").strip()
        return ("search_web", query)

    if any(word in command for word in ["exit", "quit", "stop"]):
        return ("exit", None)

    return ("unknown", None)
