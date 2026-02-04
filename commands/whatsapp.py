# commands/whatsapp.py
import pywhatkit
import time

def send_whatsapp_message(phone_number: str, message: str):
    """
    Sends a WhatsApp message instantly using WhatsApp Web.
    Phone number must include country code, e.g. +9198XXXXXXXX
    """
    # Small delay to allow browser focus
    pywhatkit.sendwhatmsg_instantly(
        phone_no=phone_number,
        message=message,
        wait_time=10,
        tab_close=True
    )
    time.sleep(2)
