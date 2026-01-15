from newspaper import Article, Config
import requests
from bs4 import BeautifulSoup

config = Config()
url = "https://fr.wikipedia.org/wiki/Le_Monde"

# article = Article(url, language='fr', config=config)
# article.download()
# article.parse()

# content = article.title + "\n" + article.text

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
paragraphs = soup.find_all("p")

print(paragraphs)

content = "\n".join(p.get_text() for p in paragraphs)

with open("test_scraping.txt", "w", encoding="utf-8") as f:
    f.write(content)