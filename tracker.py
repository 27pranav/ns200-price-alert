import json
import os
import re

import requests
from bs4 import BeautifulSoup

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": message
        }
    )


def get_flipkart_price(url):

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 Chrome/138.0 Safari/537.36"
        )
    }

    response = requests.get(url, headers=headers, timeout=20)

    soup = BeautifulSoup(response.text, "lxml")

    text = soup.get_text(" ", strip=True)

    match = re.search(r"₹\s*([\d,]+)", text)

    if not match:
        return None

    price = int(match.group(1).replace(",", ""))

    return price


with open("config.json") as f:
    config = json.load(f)

for product in config["products"]:

    current_price = get_flipkart_price(product["url"])

    print(product["name"])
    print(current_price)

    if current_price is None:
        continue

    if current_price <= product["target_price"]:

        send_telegram(
            f"""🏍️ NS200 PRICE ALERT

Your target price has been reached!

{product['name']}"""
        )