from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.llm_service import generate_response

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    model: str = "openai"  # or "local"

class ChatResponse(BaseModel):
    response: str

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        response = generate_response(request.message, request.model)
        return ChatResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
