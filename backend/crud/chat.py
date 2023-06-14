from sqlalchemy.orm import Session

from core.db.models import Chat, User
from exceptions.not_found import ChatNotFoundException
from schemas.chat import Chat as ChatSchema


def get_chats(session: Session):
    return session.query(Chat).filter(Chat.removed == False).all()


def get_chat_by_id(session: Session, chat_id: int) -> Chat:
    chat = session.query(Chat).filter((Chat.id == chat_id) & (Chat.removed == False)).first()
    if chat is None:
        raise ChatNotFoundException
    return chat


def create_chat(session: Session, chat: ChatSchema, user: User) -> Chat:
    new_chat = Chat(name=chat.name, type=chat.chat_type)
    new_chat.users.append(user)
    session.add(new_chat)
    session.commit()
    session.refresh(new_chat)
    return new_chat


def change_name_chat_by_id(session: Session, chat_id: int, new_name: str) -> str:
    chat = get_chat_by_id(session, chat_id)
    prev_name = chat.name
    chat.name = new_name
    session.commit()
    return prev_name


def delete_chat_by_id(session, chat_id: int) -> Chat:
    chat = get_chat_by_id(session, chat_id)
    chat.removed = True
    session.commit()
    return chat
