from playwright.sync_api import sync_playwright
import re


def get_price(url):

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True
        )

        page = browser.new_page(
            viewport={"width": 1400, "height": 1000}
        )

        print("Opening Flipkart...")

        page.goto(
            url,
            wait_until="domcontentloaded",
            timeout=60000
        )

        print("Waiting for page...")

        page.wait_for_timeout(5000)

        text = page.locator("body").inner_text()

        browser.close()

        prices = re.findall(r"₹\s?([\d,]+)", text)

        print(prices)

        return prices