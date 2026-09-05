from fastapi import APIRouter
from app.schemas import AgentRequest
from app.services.agent_service import answer_question

router = APIRouter()

@router.post("/chat")
def chat(data: AgentRequest):
    return {"answer": answer_question(data.question), "agent": "FinPilot AI"}
