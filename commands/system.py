import os
import json

APPS_FILE = "config/apps.json"


def load_apps():
    try:
        with open(APPS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}


def find_app(app_name: str):
    apps = load_apps()
    app_name = app_name.lower().strip()

    for key, value in apps.items():
        if app_name == key:
            return value

        aliases = [a.lower() for a in value.get("aliases", [])]
        if app_name in aliases:
            return value

    return None



def open_application(app_name: str):
    app = find_app(app_name)

    if app and "open" in app:
        os.system(app["open"])
        return True
    return False


def close_application(app_name: str):
    app = find_app(app_name)

    if app and "process" in app:
        result = os.system(f'taskkill /f /im {app["process"]} >nul 2>&1')
        return result == 0

    return False



def exit_donna():
    exit()
