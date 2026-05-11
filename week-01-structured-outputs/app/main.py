from fastapi import FastAPI
from app.api.v1.extraction import router as extraction_router

app = FastAPI(
    title="Applied AI Engineering Bootcamp",
    description="Week 1: Structured Outputs with OpenAI & Pydantic",
    version="1.0.0"
)

# Include the router with a prefix and tags for clean Swagger docs
app.include_router(
    extraction_router,
    prefix="/api/v1/extract",
    tags=["Extraction"]
)

@app.get("/health")
async def health_check():
    return {"status": "online", "version": "1.0.0"}