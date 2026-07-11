import chromadb

def connect():
    client = chromadb.PersistentClient(path="chroma_db")
    return client
