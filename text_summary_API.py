from fastapi import FastAPI
from pydantic import BaseModel

textSummarize = FastAPI()

class ArticlesInput(BaseModel):
    title: str | None
    content: str
    utl: str | None
    author: str | None





@textSummarize.post("/article")
def summarize_article(article: ArticlesInput):
    """
    Sumarize the input article and return in the data base the article with:
        - id
        - title
        - content
        - summarize
        - url
        - author
    """
    article_with_summarize = article.model_copy(update={
        "id": 1,
        "title": article.title or "Unknown",
        "url": article.url or "Unknown",
        "author": article.author or "Unknown",
        "summarize": article.content[:100]
    })

    return article_with_summarize
