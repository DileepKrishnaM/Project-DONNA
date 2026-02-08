# commands/reminder.py

REMINDER_FILE = "data/reminders.txt"

def add_reminder(text: str):
    with open(REMINDER_FILE, "a", encoding="utf-8") as f:
        f.write(text + "\n")

def get_reminders():
    try:
        with open(REMINDER_FILE, "r", encoding="utf-8") as f:
            reminders = f.readlines()
            return [r.strip() for r in reminders if r.strip()]
    except FileNotFoundError:
        return []
