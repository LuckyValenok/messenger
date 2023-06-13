from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Text
from sqlalchemy.orm import relationship, class_mapper
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def serialize(model):
    columns = [c.key for c in class_mapper(model.__class__).columns]
    return dict((c, f'{getattr(model, c)}') for c in columns)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String, unique=True)
    password = Column(String)
    name = Column(String)
    deleted = Column(Boolean, nullable=False, default=False)

    chats = relationship("Chat", secondary="users_chats")


class Chat(Base):
    __tablename__ = "chats"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    created_date = Column(DateTime, server_default=func.now())
    type = Column(String)
    removed = Column(Boolean, nullable=False, default=False)

    users = relationship("User", secondary="users_chats", overlaps="chats")
    messages = relationship(
        "Message", secondary="users_chats", primaryjoin="Chat.id == UserChat.chat_id",
        secondaryjoin="Message.user_chat_id == UserChat.id"
    )


class UserChat(Base):
    __tablename__ = "users_chats"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(f'{User.__tablename__}.id'))
    chat_id = Column(Integer, ForeignKey(f'{Chat.__tablename__}.id'))

    messages = relationship("Message")


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    user_chat_id = Column(Integer, ForeignKey(f'{UserChat.__tablename__}.id'))
    text = Column(Text)
    created_date = Column(DateTime, server_default=func.now())
    edited = Column(Boolean, nullable=False, default=False)
    read = Column(Boolean, nullable=False, default=False)

    user = relationship(
        "User", secondary="users_chats", primaryjoin="Message.user_chat_id == UserChat.id",
        secondaryjoin="User.id == UserChat.user_id", uselist=False
    )
