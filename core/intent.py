# core/intent.py

def parse_intent(command: str):
    command = command.lower()

    if "whatsapp" in command and "send" in command:
        if "to" in command and "saying" in command:
            to_part = command.split("to", 1)[1]
            name, message = to_part.split("saying", 1)
            return ("send_whatsapp", {
                "name": name.strip(),
                "message": message.strip()
            })
        return ("send_whatsapp", None)

    if any(word in command for word in ["open", "launch", "start"]):
        if "chrome" in command:
            return ("open_app", "chrome")

    if any(word in command for word in ["search", "google", "find"]):
        query = command.replace("search", "").replace("google", "").strip()
        return ("search_web", query)

    if any(word in command for word in ["exit", "quit", "stop"]):
        return ("exit", None)

    return ("unknown", None)
