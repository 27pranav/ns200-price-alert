from utils import load_config
import flipkart

config = load_config()

product = config["products"][0]

flipkart.get_price(product["url"])