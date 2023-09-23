import time
import html
import requests,json
import os
api = "https://opentdb.com/api.php?amount=30&category=18&type=boolean"
print(html.unescape("&quot;Hello World&quot;"))
data = requests.get(api).json()["results"]

with open("data.json", "w") as f:
    json.dump(data,f, indent=4)

