import requests
import os
import json
from newspaper import Article, Config
from bs4 import BeautifulSoup

API_KEY = "92f835d89dd44cc9b70ebae91db2554f"
NEWS_API_URL = "https://newsapi.org/v2/top-headlines"
articles_path = os.path.join("datas", "input", "articles_fetched.json")


def fetch_articles():
    params = {
        "from": "2026-01-01",
        "country": "us",
        "category": "technology",
        "apiKey": API_KEY
    }

    response = requests.get(NEWS_API_URL, params=params)
    response.raise_for_status()



    return response.json().get("articles", [])


def write_json(data, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def get_full_article_content_soup(url):
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        paragraphs = soup.find_all("p")

        return "\n".join(p.get_text() for p in paragraphs)
    except Exception as e:
        print(f"Failed to fetch {url} with newspaper3k: {e}")
        return ""


def get_full_article_content_newspaper3k(url):
    try:
        config = Config()
        article = Article(url, language='en', config=config)
        article.download()
        article.parse()

        return article.text
    except Exception as e:
        print(f"Failed to fetch {url} with newspaper3k: {e}")
        return ""


def get_all_full_content(articles):
    full_articles = []
    for article in articles:
        article_url = article['url']

        soup_content = get_full_article_content_soup(article_url)
        newspaper_content = get_full_article_content_newspaper3k(article_url)
        new_content = soup_content if len(soup_content) > len(newspaper_content) else newspaper_content

        article['content'] = new_content
        full_articles.append(article)
    return full_articles

def main():
    articles = fetch_articles()
    full_articles = get_all_full_content(articles)
    

    final_articles_path = os.path.join("datas", "input", "articles_fetched.json")
    write_json(full_articles, final_articles_path)


if __name__ == "__main__":
    main()
