import requests, os

def send_telegram(command):
    BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
    message = command.split("telegram:")[-1].strip()
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    r = requests.post(url, json=data)
    return "Sent to Telegram" if r.status_code == 200 else "Failed"
