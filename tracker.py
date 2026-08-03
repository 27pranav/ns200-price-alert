from utils import load_config
import flipkart

config = load_config()

product = config["products"][0]

prices = flipkart.get_price(product["url"])

print("\nPrices found on page:\n")

for p in prices[:20]:
    print(p)