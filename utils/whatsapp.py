from twilio.rest import Client
import os

def send_whatsapp(command):
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)
    message = command.split("whatsapp:")[-1].strip()
    msg = client.messages.create(
        from_='whatsapp:+14155238886',
        body=message,
        to=os.getenv("WHATSAPP_TO")
    )
    return "WhatsApp message sent."
