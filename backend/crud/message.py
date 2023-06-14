from sqlalchemy.orm import Session

from core.db.models import Message, UserChat
from crud.chat import get_chat_by_id
from exceptions.validation import UserDontHavePermissionsException


def get_messages_in_chat(session: Session, chat_id: int):
    return get_chat_by_id(session, chat_id).messages


def create_message(session: Session, user_id: int, chat_id: int, text: str):
    user_chat = session.query(UserChat).filter(
        (UserChat.user_id == user_id) & (UserChat.chat_id == chat_id)).one()
    if user_chat is None:
        raise UserDontHavePermissionsException
    message = Message(text=text)
    user_chat.messages.append(message)
    session.commit()
    session.refresh(message)
    return message
