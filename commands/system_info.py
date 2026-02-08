# commands/system_info.py
from datetime import datetime
import psutil

def get_time():
    return datetime.now().strftime("%I:%M %p")

def get_date():
    return datetime.now().strftime("%A, %d %B %Y")

def get_battery():
    battery = psutil.sensors_battery()
    if battery:
        return f"Battery is at {battery.percent} percent."
    return "Battery information is not available."
