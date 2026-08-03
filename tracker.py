from utils import load_config
import flipkart

config = load_config()

product = config["products"][0]

prices = flipkart.get_price(product["url"])

if prices:
    print(f"\nLowest detected bike price: ₹{min(prices):,}")
else:
    print("No valid bike prices found.")
