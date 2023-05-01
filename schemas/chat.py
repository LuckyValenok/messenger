from datetime import datetime

from pydantic import BaseModel


class Chat(BaseModel):
    name: str
    type: str
    created_date: datetime


class ChatInDB(Chat):
    id: int

    class Config:
        orm_mode = True
