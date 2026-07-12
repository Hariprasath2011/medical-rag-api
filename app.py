from fastapi import FastAPI
from fastapi import UploadFile
from services.pdf_service import extract_text
from services.chroma_service import connect

from services.chunk_service import create_chunks

app = FastAPI()

client = connect()

@app.post("/ingest")
async def ingest(file: UploadFile):

    text = extract_text(file)

    chunks = create_chunks(text)

    return {
        "filename": file.filename,
        "characters": len(text),
        "chunks": len(chunks),
        "first_chunk": chunks[0]
    }

@app.get("/collections")
def collections():

    names = []

    for c in client.list_collections():
        names.append(c.name)

    return {
        "collections": names
    }
