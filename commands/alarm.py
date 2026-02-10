# commands/alarm.py
from datetime import datetime
import time

ALARM_FILE = "data/alarms.txt"

def add_alarm(time_str: str):
    time_str = normalize_time(time_str)
    with open(ALARM_FILE, "a", encoding="utf-8") as f:
        f.write(time_str + "\n")

def normalize_time(time_str: str):
    """
    Converts formats like '1942' to '19:42'
    Keeps valid HH:MM unchanged.
    """
    time_str = time_str.strip()

    if ":" in time_str:
        return time_str

    if len(time_str) == 4 and time_str.isdigit():
        return time_str[:2] + ":" + time_str[2:]

    return time_str

def check_alarms(speak):
    """
    Continuously checks alarms in background.
    """
    while True:
        try:
            now = datetime.now().strftime("%H:%M")

            with open(ALARM_FILE, "r", encoding="utf-8") as f:
                alarms = f.readlines()

            remaining = []
            for alarm in alarms:
                alarm_time = alarm.strip()
                if alarm_time == now:
                    speak("Alarm ringing.")
                else:
                    remaining.append(alarm)

            with open(ALARM_FILE, "w", encoding="utf-8") as f:
                f.writelines(remaining)

        except:
            pass

        time.sleep(1)

def clear_alarms():
    with open(ALARM_FILE, "w", encoding="utf-8") as f:
        f.write("")
