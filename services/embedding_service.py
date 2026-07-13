from langchain_huggingface import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-m3"
)

def embed_documents(texts):
    return embedding_model.embed_documents(texts)
