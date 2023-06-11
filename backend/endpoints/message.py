from fastapi import APIRouter

from crud.message import get_messages_in_chat as crud_get_messages_in_chat, create_message as crud_create_message
from schemas.message import Message

router = APIRouter(prefix="/message")


@router.get("/get/{chat_id}")
async def get_messages_in_chat(chat_id: int):
    return crud_get_messages_in_chat(chat_id)


@router.post("/new")
async def create_message(message: Message):
    return crud_create_message(message)
