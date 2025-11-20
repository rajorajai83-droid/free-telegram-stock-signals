import os
import time
from telegram import Bot
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = "@YOUR_CHANNEL_ID"   # change this

bot = Bot(token=BOT_TOKEN)

def get_chart(symbol):
    url = f"https://www.tradingview.com/chart/?symbol={symbol}"

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.get(url)
    time.sleep(5)

    driver.save_screenshot("chart.png")
    driver.quit()

    return "chart.png"

def send_signal(symbol):
    chart = get_chart(symbol)

    bot.send_photo(
        chat_id=CHAT_ID,
        photo=open(chart, "rb"),
        caption=f"📈 *{symbol} Chart Update*\nAuto-generated Signal Bot",
        parse_mode="Markdown"
    )

send_signal("NSE:RELIANCE")
