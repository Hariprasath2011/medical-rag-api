from fastapi import FastAPI
from fastapi import UploadFile

from services.chroma_service import connect

app = FastAPI()

client = connect()

@app.post("/ingest")
async def ingest(file: UploadFile):

    return {
        "filename": file.filename,
        "content_type": file.content_type
    }

@app.get("/")
def root():

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
