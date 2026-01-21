from fastapi import FastAPI
from pydantic import BaseModel

textSummarize = FastAPI()

class ArticlesInput(BaseModel):
    title: str | None
    content: str
    url: str | None
    author: str | None
    summary: str | None = None
    id: int | None = None


@textSummarize.post("/article")
def summarize_article(article: ArticlesInput):
    """
    Sumarize the input article and return in the data base the article with:
        - id
        - title
        - content
        - summary
        - url
        - author
    """
    article_with_summarize = article.model_copy(update={
        "id": 1,
        "title": article.title or "Unknown",
        "url": article.url or "Unknown",
        "author": article.author or "Unknown",
        "summary": "this is a summary"
    })

    return article_with_summarize
