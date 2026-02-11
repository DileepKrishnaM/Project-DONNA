# commands/volume.py
import pyautogui

def increase_volume(steps=5):
    for _ in range(steps):
        pyautogui.press("volumeup")

def decrease_volume(steps=5):
    for _ in range(steps):
        pyautogui.press("volumedown")

def mute_volume():
    pyautogui.press("volumemute")
