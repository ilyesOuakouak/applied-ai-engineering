from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    question: str = Field(description="The question that will be asked by the user.")

class IngestRequest(BaseModel):
    text: str = Field(description="The raw document text that will be converted into an embedding and stored in ChromaDB.")
