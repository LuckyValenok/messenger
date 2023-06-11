from enum import Enum

from pydantic import BaseModel


class ChatType(str, Enum):
    public = "public"
    private = "private"
    group = "group"


class Chat(BaseModel):
    name: str
    type: ChatType

    class Config:
        orm_mode = True
