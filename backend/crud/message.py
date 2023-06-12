from fastapi import HTTPException, status

from core.db.models import Message, UserChat
from core.db.session import get_session
from crud.chat import get_chat_by_id
from schemas.message import Message as MessageSchema


def get_messages_in_chat(chat_id: int):
    return get_chat_by_id(chat_id).messages


def create_message(message: MessageSchema):
    try:
        user_chat = get_session().query(UserChat).filter(
            (UserChat.user_id == message.user_id) & (UserChat.chat_id == message.chat_id)).one()
        if user_chat is None:
            raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)
        message = Message(text=message.text)
        user_chat.messages.append(message)
        return message
    finally:
        get_session().commit()
