from enum import Enum

from core.db.models import Chat
from core.db.session import get_session


class ChatType(str, Enum):
    public = "public"
    private = "private"
    group = "group"


def get_chats() -> dict:
    return get_session().query(Chat).all()


def get_chat_by_id(chat_id: int) -> Chat:
    return get_session().query(Chat).filter_by(id=chat_id).first()


def create_new_chat(chat) -> Chat:
    try:
        new_chat = Chat(name=chat.name, type=chat.type, created_date=chat.created_date)
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
        return get_session().query(Chat).filter_by(id=chat_id).delete()
    finally:
        get_session().commit()
