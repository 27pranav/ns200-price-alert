from playwright.sync_api import sync_playwright


def get_price(url):
    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True
        )

        page = browser.new_page()

        page.goto(
            url,
            wait_until="domcontentloaded",
            timeout=60000
        )

        print("Flipkart page opened successfully")

        browser.close()