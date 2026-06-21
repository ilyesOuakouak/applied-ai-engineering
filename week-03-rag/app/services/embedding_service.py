import uuid

import chromadb

client = chromadb.PersistentClient(path="./chroma_data")
collection = client.get_or_create_collection(name="documents")

def add_document(text: str):
    unique_id = str(uuid.uuid4())
    collection.add(
        documents=[text],
        ids=[unique_id]  # needs to be unique per document
    )

    return {"status": "success", "id": unique_id}

def query_documents(question: str, n_results: int = 3):
    results = collection.query(
        query_texts=[question],
        n_results=n_results
    )
    return results