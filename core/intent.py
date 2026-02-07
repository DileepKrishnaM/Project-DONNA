# core/intent.py

def parse_intent(command: str):
    command = command.lower()

    # ---- OPEN APPLICATION ----
    open_keywords = ["open", "launch", "start", "run"]
    if any(word in command for word in open_keywords):
        if "chrome" in command:
            return ("open_app", "chrome")

    # ---- SEARCH WEB ----
    search_keywords = ["search", "find", "google", "look up"]
    if any(word in command for word in search_keywords):
        # Remove common filler words
        cleaned = command
        for word in ["search", "find", "google", "look up", "for"]:
            cleaned = cleaned.replace(word, "")
        query = cleaned.strip()
        return ("search_web", query)

    # ---- WHATSAPP ----
    if "whatsapp" in command and "send" in command:
        if "to" in command and "saying" in command:
            try:
                to_part = command.split("to", 1)[1]
                name, message = to_part.split("saying", 1)
                return ("send_whatsapp", {
                    "name": name.strip(),
                    "message": message.strip()
                })
            except:
                return ("send_whatsapp", None)

    # ---- EXIT ----
    if any(word in command for word in ["exit", "quit", "stop"]):
        return ("exit", None)

    return ("unknown", None)
