# core/intent.py

from click import command


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
        
    # -- PLAY MUSIC ----
    play_keywords = ["play", "listen to"]
    if any(word in command for word in play_keywords):
        cleaned = command
        for word in ["play", "listen to"]:
            cleaned = cleaned.replace(word, "")
        song = cleaned.strip()

        if song:
            return ("play_music", song)
        else:
            return ("play_music", "music")
        
    # ---- VOLUME CONTROL ----
    if "increase volume" in command or "volume up" in command:
        return ("volume_up", None)

    if "decrease volume" in command or "volume down" in command:
        return ("volume_down", None)

    if "mute" in command:
        return ("volume_mute", None)


    # ---- TIME ----
    if "time" in command:
        return ("get_time", None)

    # ---- DATE ----
    if "date" in command or "today" in command:
        return ("get_date", None)

    # ---- BATTERY ----
    if "battery" in command:
        return ("get_battery", None)

    # ---- REMINDER ADD ----
    if "remind me to" in command:
        reminder_text = command.split("remind me to", 1)[1].strip()
        return ("add_reminder", reminder_text)

    # ---- REMINDER LIST ----
    if "my reminders" in command or "my tasks" in command:
        return ("list_reminders", None)

    # ---- ALARM ----
    if "set alarm for" in command:
        time_text = command.split("set alarm for", 1)[1].strip()
        return ("set_alarm", time_text)

    # ---- CANCEL ALARM ----
    if "cancel alarm" in command or "clear alarms" in command:
        return ("clear_alarms", None)

    # ---- CANCEL SHUTDOWN / RESTART ----
    if "cancel shutdown" in command or "abort shutdown" in command or "cancel restart" in command:
        return ("cancel_shutdown", None)
    
    # ---- RESTART ----
    if "restart" in command or "reboot" in command:
        return ("restart", None)

    # ---- SHUTDOWN ----
    if "shutdown" in command or "shut down" in command:
        return ("shutdown", None)
    
    # ---- OPEN APPLICATION ----
    open_keywords = ["open", "launch", "start", "run"]
    for keyword in open_keywords:
        if keyword in command:
            app_name = command.split(keyword, 1)[1].strip()
            return ("open_app", app_name)

    # ---- CLOSE APPLICATION ----
    if "close" in command:
        app_name = command.split("close", 1)[1].strip()
        return ("close_app", app_name)


    # ---- EXIT ----
    if any(word in command for word in ["exit", "quit", "stop"]):
        return ("exit", None)

    return ("unknown", None)
