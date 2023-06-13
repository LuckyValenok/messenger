from datetime import datetime
from enum import Enum

from pydantic import BaseModel

from schemas.message import MessageWithUserOutScheme


class ChatType(str, Enum):
    public = "public"
    private = "private"
    group = "group"


class Chat(BaseModel):
    name: str
    type: ChatType

    class Config:
        orm_mode = True


class ChatOutScheme(BaseModel):
    id: int
    name: str
    type: ChatType
    created_date: datetime
    removed: bool

    class Config:
        orm_mode = True


class ChatWithLastMessageOutScheme(ChatOutScheme):
    message: MessageWithUserOutScheme

    class Config:
        orm_mode = True


class ChatWithMessagesOutScheme(ChatOutScheme):
    messages: list[MessageWithUserOutScheme]

    class Config:
        orm_mode = True
