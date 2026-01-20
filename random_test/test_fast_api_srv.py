from fastapi import FastAPI
import requests

app = FastAPI()


# ============= Exemple 1 GET ==============


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


# ============= Exemple 2 POST ==============


@app.post("/sayhello")
def say_hello(text: str):
    return {
        "response": "f{text} World"
    }