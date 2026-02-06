# Project DONNA

A voice-controlled personal AI assistant that listens for a wake word, understands spoken commands, and performs everyday desktop tasks like opening applications, searching the web, and sending WhatsApp messages.

---

## Features

* Wake-word activation ("Jarvis")
* Speech-to-text command recognition
* Natural voice responses
* Open desktop applications
* Web search via voice
* WhatsApp messaging through voice commands
* Intent-based command parsing
* Modular and extensible architecture

---

## Example Commands

Jarvis → open chrome
Jarvis → search operating systems
Jarvis → send whatsapp message saying hello

---

## Project Structure

core/ – speech, intent parsing, command routing
commands/ – task execution modules
config/ – configuration and contacts
main.py – entry point

---

## Installation

Install dependencies:

pip install -r requirements.txt

Run the assistant:

python main.py

---

## Notes

Personal contacts are stored locally in `config/contacts.json`, which is ignored by Git to keep private data safe.

---

## Status

Under active development.
