from core.db.models import Message, UserChat
from core.db.session import get_session
from crud.chat import get_chat_by_id
from exceptions.validation import UserDontHavePermissionsException


def get_messages_in_chat(chat_id: int):
    return get_chat_by_id(chat_id).messages


def create_message(user_id: int, chat_id: int, text: str):
    try:
        user_chat = get_session().query(UserChat).filter(
            (UserChat.user_id == user_id) & (UserChat.chat_id == chat_id)).one()
        if user_chat is None:
            raise UserDontHavePermissionsException
        message = Message(text=text)
        user_chat.messages.append(message)
        return message
    finally:
        get_session().commit()
