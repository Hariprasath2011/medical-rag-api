from fastapi import FastAPI
from services.chroma_service import connect

app = FastAPI(
    title="Medical RAG API",
    version="1.0.0"
)

client = connect()


@app.get("/")
def home():
    return {
        "status": "Medical RAG API Running"
    }


@app.get("/collections")
def collections():

    names = []

    for c in client.list_collections():
        names.append(c.name)

    return {
        "collections": names
    }
