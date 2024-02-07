import requests
from config import BOT_TOKEN, CHAT_ID


token = BOT_TOKEN
chat_id = CHAT_ID


def send_message(text):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {"chat_id": chat_id, "text": text}
    requests.get(url, params=params)
