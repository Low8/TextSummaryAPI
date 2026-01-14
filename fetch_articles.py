import requests
import os
import json

API_KEY = "92f835d89dd44cc9b70ebae91db2554f"


url = 'https://newsapi.org/v2/top-headlines?'

params = {
    "q": "technology",
    "from": "2026-01-10",
    "apikey": API_KEY
}

response = requests.get(url, params=params)

path = os.path.join('datas', 'input', 'articles_fetched.json')
os.makedirs(os.path.dirname(path), exist_ok=True)

with open(path, 'w') as f:
    json.dump(response.json(), f, indent=4)

print(response.json())