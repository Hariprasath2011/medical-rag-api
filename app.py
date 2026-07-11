from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "status": "Medical RAG API Running"
    }
