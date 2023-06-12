from fastapi import APIRouter, HTTPException, status

from crud.message import get_messages_in_chat as crud_get_messages_in_chat, create_message as crud_create_message
from schemas.message import Message, MessageWithUserOutScheme, MessageOutScheme

router = APIRouter(prefix="/message")


@router.get("/get/{chat_id}", response_model=list[MessageWithUserOutScheme])
async def get_messages_in_chat(chat_id: int):
    messages = crud_get_messages_in_chat(chat_id)
    if messages is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    for message in messages:
        message.user
    return messages


@router.post("/new")
async def create_message(message: Message):
    return crud_create_message(message)


@router.get("/last/{chat_id}", response_model=MessageOutScheme)
async def get_last_message_in_chat(chat_id: int):
    messages = crud_get_messages_in_chat(chat_id)
    if messages is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if len(messages) == 0:
        return []
    else:
        return messages[0]
