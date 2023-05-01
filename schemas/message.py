from datetime import datetime

from pydantic import BaseModel


class Message(BaseModel):
    user_id: int
    chat_id: int
    text: str
    created_date: datetime


class MessageInDB(Message):
    id: int

    class Config:
        orm_mode = True
