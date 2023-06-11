from fastapi import APIRouter, Depends, HTTPException, status

from core.db.models import Chat
from core.db.session import get_session
from schemas.chat import Chat as ChatSchema


def get_chats():
    return get_session().query(Chat).filter(Chat.removed == False).all()


def get_chat_by_id(chat_id: int) -> Chat:
    chat = get_session().query(Chat).filter((Chat.id == chat_id) & (Chat.removed == False)).first()
    if chat is None:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)
    return chat


def create_chat(chat: ChatSchema) -> Chat:
    try:
        new_chat = Chat(name=chat.name, type=chat.type)
        get_session().add(new_chat)
        return new_chat
    finally:
        get_session().commit()


def change_name_chat_by_id(chat_id: int, new_name: str) -> str:
    try:
        chat = get_chat_by_id(chat_id)
        prev_name = chat.name
        chat.name = new_name
        return prev_name
    finally:
        get_session().commit()


def delete_chat_by_id(chat_id: int) -> Chat:
    try:
        chat = get_chat_by_id(chat_id)
        chat.removed = True
        return chat
    finally:
        get_session().commit()
