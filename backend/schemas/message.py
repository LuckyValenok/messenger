from datetime import datetime

from pydantic import BaseModel

from schemas.user import UserWithoutPassword


class Message(BaseModel):
    user_id: int
    chat_id: int
    text: str

    class Config:
        orm_mode = True


class MessageOutScheme(BaseModel):
    id: int
    text: str
    edited: bool
    read: bool
    created_date: datetime

    class Config:
        orm_mode = True


class MessageWithUserOutScheme(MessageOutScheme):
    user: UserWithoutPassword

    class Config:
        orm_mode = True
