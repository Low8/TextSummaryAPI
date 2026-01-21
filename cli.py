import os
import json
import requests
url = "http://127.0.0.1:8000/article"

json_path = os.path.join("datas", "input", "articles_fetched.json")

with open(json_path, "r", encoding="utf-8") as f:
    articles = json.load(f)

print(articles[0])