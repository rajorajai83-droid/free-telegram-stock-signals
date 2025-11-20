import os
import requests
import telegram
from datetime import datetime

BOT_TOKEN = os.getenv("8235242533:AAHxgo3Z2RycfHLu7uWpx_RuowzEIzS1npU")
CHAT_ID = os.getenv("-1003330906337")

def send_signal():
    url = "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%2050"
    headers = {"User-Agent": "Mozilla/5.0"}

    data = requests.get(url, headers=headers).json()
    stocks = data["data"][:3]

    message = "📈 *Free Intraday Signals — India Market*\n"
    message += f"🕒 {datetime.now().strftime('%I:%M %p')}\n\n"

    for s in stocks:
        message += f"• {s['symbol']} — {s['lastPrice']} ({s['pChange']}%)\n"

    bot = telegram.Bot(token=BOT_TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=message, parse_mode="Markdown")

send_signal()
