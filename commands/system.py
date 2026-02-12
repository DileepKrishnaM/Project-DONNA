# commands/system.py
import os

def open_application(app_name: str):
    apps = {
        "chrome": "start chrome",
        "notepad": "start notepad",
        "calculator": "start calc",
        "paint": "start mspaint"
    }

    command = apps.get(app_name.lower())

    if command:
        os.system(command)
        return True
    return False


def exit_donna():
    exit()

def close_application(app_name: str):
    """
    Closes an application by process name (Windows).
    """
    processes = {
        "chrome": "chrome.exe",
        "notepad": "notepad.exe"
    }

    process = processes.get(app_name.lower())

    if process:
        os.system(f"taskkill /f /im {process}")
        return True
    return False
