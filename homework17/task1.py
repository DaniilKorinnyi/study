import requests
import random

sites = ["google.com", "facebook.com", "twitter.com", "amazon.com", "apple.com"]
site = random.choice(sites)

response = requests.get(f"https://{site}")

print(f"Site: {site}")
print(f"Status code: {response.status_code}")
print(f"Content length: {len(response.text)}")
