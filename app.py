import uuid

from fastapi import FastAPI, UploadFile, HTTPException

from services.pdf_service import extract_text
from services.chunk_service import create_chunks
from services.embedding_service import embed_documents
from services.chroma_service import get_collection

app = FastAPI(
    title="Medical RAG API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "status": "Medical RAG API Running"
    }


@app.post("/ingest")
async def ingest(file: UploadFile):

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported."
        )

    # Extract text
    text = extract_text(file)

    if not text.strip():
        raise HTTPException(
            status_code=400,
            detail="No text found inside PDF."
        )

    # Split into chunks
    chunks = create_chunks(text)

    # Generate embeddings
    embeddings = embed_documents(chunks)

    # Connect to ChromaDB
    collection = get_collection()

    # Generate unique IDs
    ids = [str(uuid.uuid4()) for _ in chunks]

    # Store in Chroma
    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=[
            {
                "filename": file.filename,
                "chunk": i
            }
            for i in range(len(chunks))
        ]
    )

    return {
        "status": "success",
        "filename": file.filename,
        "characters": len(text),
        "chunks": len(chunks),
        "stored": len(chunks)
    }


@app.get("/collections")
def collections():

    collection = get_collection()

    return {
        "collections": [
            collection.name
        ]
    }
@app.get("/collections")
def collections():

    names = []

    for c in client.list_collections():
        names.append(c.name)

    return {
        "collections": names
    }
