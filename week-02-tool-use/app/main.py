from fastapi import FastAPI
from app.api.v1.agent import router as agent_router

app = FastAPI(title="Applied AI Engineering Blueprint")
# Register the v1 agent router
app.include_router(agent_router, prefix="/api/v1/agent", tags=["Agent"])

@app.get("/health")
def health_check():
    return {"status": "healthy"}