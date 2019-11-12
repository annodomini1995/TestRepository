import requests
import pprint

page = requests.get("https://www.google.com")
print(page.content)