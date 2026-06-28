from fastapi import APIRouter, HTTPException

from core.responses import success
from services.chatbot import chatbot
from services.learning import learn
from services.memory import get_memory

router = APIRouter(
    prefix="/ai",
    tags=["AI"],
)


@router.get("/")
async def info():
    return success(
        message="AI service is running.",
        data={
            "service": "AI",
            "status": "ready",
        },
    )


@router.post("/chat")
async def chat(payload: dict):

    try:
        message = payload.get("message", "")

        response = chatbot(message)

        return success(
            message="Response generated successfully.",
            data={
                "response": response,
            },
        )

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=str(exc),
        )


@router.post("/learn")
async def learning(payload: dict):

    try:
        learn(payload)

        return success(
            message="Knowledge stored successfully.",
        )

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=str(exc),
        )


@router.get("/memory")
async def memory():

    return success(
        data=get_memory(),
    )
