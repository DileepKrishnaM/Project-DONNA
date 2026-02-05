# core/contacts.py
import json
from pathlib import Path

CONTACTS_FILE = Path("config/contacts.json")

def get_contact_number(name: str):
    if not CONTACTS_FILE.exists():
        return None

    with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
        contacts = json.load(f)

    return contacts.get(name.lower())
