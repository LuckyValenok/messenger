from fastapi import APIRouter, Depends

from core.db.models import User
from crud.chat import get_chat_by_id
from crud.message import create_message as crud_create_message
from deps import get_current_user
from endpoints.websocket import manager
from exceptions.validation import UserDontHavePermissionsException
from schemas.message import MessageWithUserOutScheme, MessageOutScheme

router = APIRouter(prefix="/message")


@router.get("/get/{chat_id}", response_model=list[MessageWithUserOutScheme])
async def get_messages_in_chat(chat_id: int, user: User = Depends(get_current_user)):
    chat = get_chat_by_id(chat_id)
    if user not in chat.users:
        raise UserDontHavePermissionsException
    messages = chat.messages
    for message in messages:
        message.user
    return messages


@router.post("/new", response_model=MessageWithUserOutScheme)
async def create_message(chat_id: int, text: str, user: User = Depends(get_current_user)):
    message = crud_create_message(user.id, chat_id, text)
    try:
        return message
    finally:
        await manager.broadcast(
            MessageWithUserOutScheme(id=message.id, text=message.text, edited=message.edited, read=message.read,
                                     created_date=message.created_date, user=message.user).json(), chat_id=chat_id)


@router.get("/last/{chat_id}", response_model=MessageOutScheme)
async def get_last_message_in_chat(chat_id: int, user: User = Depends(get_current_user)):
    chat = get_chat_by_id(chat_id)
    if user not in chat.users:
        raise UserDontHavePermissionsException
    messages = chat.messages
    if len(messages) == 0:
        return {}
    else:
        return messages[0]
