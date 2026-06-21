from fastapi import APIRouter
from pydantic import BaseModel
from app.schemas.document import ChatRequest,IngestRequest
from app.services.ai_service import chat_with_docs
from app.services.embedding_service import add_document

router = APIRouter()

@router.post("/ingest")
def ingest_endpoint(request: IngestRequest):
    response = add_document(text=request.text)

    return response

@router.post("/chat")
def chat_endpoint(request: ChatRequest):
    response = chat_with_docs(question=request.question)

    return response
