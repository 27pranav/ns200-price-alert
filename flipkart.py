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

        try:
            page.goto(
                url,
                wait_until="commit",
                timeout=90000
            )

            print("Navigation completed")

        except Exception as e:
            print("Navigation failed:", e)
            browser.close()
            return None

        print("Waiting for page...")

        page.wait_for_timeout(8000)

        text = page.locator("body").inner_text()

        browser.close()

        prices = re.findall(r"₹\s?([\d,]+)", text)

# Convert to integers
prices = [int(p.replace(",", "")) for p in prices]

# Keep only realistic bike prices
bike_prices = [p for p in prices if 100000 <= p <= 250000]

print("Possible bike prices:")
print(bike_prices)

browser.close()

return bike_prices
