import os
import chromadb

HOST = os.getenv("CHROMA_HOST")
PORT = int(os.getenv("CHROMA_PORT", "443"))
SSL = os.getenv("CHROMA_SSL", "true").lower() == "true"

COLLECTION_NAME = "medical_documents"


def connect():

    client = chromadb.HttpClient(
        host=HOST,
        port=PORT,
        ssl=SSL,
    )

    return client


def get_collection():

    client = connect()

    return client.get_or_create_collection(
        name=COLLECTION_NAME
    )
