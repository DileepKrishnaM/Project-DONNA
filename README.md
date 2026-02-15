# Project DONNA

### A Voice-Controlled Personal AI Assistant

Project DONNA is a modular, voice-controlled desktop assistant built in Python.
It listens, understands, and performs real tasks — turning your computer into an interactive assistant inspired by systems like JARVIS.

This project focuses on **practical automation, clean architecture, and extensibility**, making it a strong learning and portfolio project.

---

## Why Project DONNA?

Most tutorials stop at basic speech recognition.
Project DONNA goes further:

* Real command execution
* Modular architecture
* Persistent reminders and alarms
* Configurable applications
* Natural command phrasing
* System-level control

This makes it a **real assistant, not just a demo**.

---

## What DONNA Can Do

### Voice Interaction

* Wake-word activation
* Speech-to-text recognition
* Natural voice responses
* Flexible command phrasing

### Application Control

* Open applications
* Close applications
* Configurable app list (no code edits required)
* Alias support (e.g., “vs code” → VS Code)

### Web and Media

* Search the web
* Play music or videos on YouTube

### Productivity

* Save reminders
* Read reminders
* Set alarms
* Cancel alarms

### Communication

* Send WhatsApp messages using voice commands
* Contact mapping with private configuration

### System Utilities

* Tell time and date
* Battery status
* Volume control

---

## Example Commands

* Jarvis → open chrome
* Jarvis → open vs code
* Jarvis → close chrome
* Jarvis → search operating systems
* Jarvis → play lo-fi music
* Jarvis → remind me to drink water
* Jarvis → what are my reminders
* Jarvis → set alarm for 19:45
* Jarvis → increase volume

---

## Architecture Overview

The project follows a modular design:

core/

* Handles speech, parsing, and command routing

commands/

* Contains individual features (apps, alarms, reminders, media, etc.)

config/

* Stores configurable apps and contacts

data/

* Stores reminders and alarms

main.py

* Entry point and orchestration

This structure allows new commands to be added easily.

---

## Installation

Install dependencies:

pip install -r requirements.txt

Run the assistant:

python main.py

---

## Configuration

### Applications

Edit:
config/apps.json

Add applications without changing code.

### Contacts

Copy:
config/contacts.sample.json

Rename to:
config/contacts.json

Add your contacts.
This file is ignored by Git to keep personal data safe.

---

## Design Principles

* Simple and readable code
* Modular structure
* Real-world functionality
* Easy extensibility

---

## Project Value

This project demonstrates:

* System automation
* Speech interfaces
* Modular software design
* Practical Python engineering
* Real-world problem solving

It serves as both a **learning platform** and a **portfolio project**.

---

## Future Roadmap

* GUI dashboard
* Offline speech recognition
* Smart scheduling
* Plugin system
* Context awareness

---

## Status

Actively under development and continuously improving.
