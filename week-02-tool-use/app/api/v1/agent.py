from fastapi import APIRouter
from pydantic import BaseModel
from app.services.ai_service import run_agent

router = APIRouter()

class AgentRequest(BaseModel):
    user_message: str

@router.post("/agent")
def agent_endpoint(request: AgentRequest):
    result = run_agent(user_message=request.user_message)
    return {"result": result}