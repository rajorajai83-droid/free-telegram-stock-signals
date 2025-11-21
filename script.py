import os
import requests
import telegram
from datetime import datetime

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_signal():
    try:
        url = "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%2050"
        headers = {"User-Agent": "Mozilla/5.0"}

        r = requests.get(url, headers=headers)
        r.raise_for_status()

        data = r.json()

        if "data" not in data or len(data["data"]) == 0:
            message = "⚠️ NSE data unavailable right now.\nTry again later."
        else:
            stocks = data["data"][:3]

            message = "📈 *Free Intraday Signals — India Market*\n"
            message += f"🕒 {datetime.now().strftime('%I:%M %p')}\n\n"

            for s in stocks:
                message += f"• {s['symbol']} — {s['lastPrice']} ({s['pChange']}%)\n"

        bot = telegram.Bot(token=BOT_TOKEN)
        bot.send_message(chat_id=CHAT_ID, text=message, parse_mode="Markdown")

    except Exception as e:
        bot = telegram.Bot(token=BOT_TOKEN)
        bot.send_message(chat_id=CHAT_ID, text=f"❌ Error: {e}")

send_signal()
