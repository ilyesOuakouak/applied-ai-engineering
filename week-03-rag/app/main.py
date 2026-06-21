from fastapi import FastAPI
from app.api.v1.rag import router as rag_router

app = FastAPI(title="Applied AI Engineering Blueprint")

# Register the v1 agent router
app.include_router(rag_router, prefix="/api/v1/rag", tags=["ingest", "chat"])

@app.get("/health")
def health_check():
    return {"status": "healthy"}