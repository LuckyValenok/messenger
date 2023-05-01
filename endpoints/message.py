from fastapi import APIRouter

from crud.message import message_database
from schemas.message import Message, MessageInDB

router = APIRouter(prefix="/message")


@router.get("/{message_id}")
async def get_message(message_id: int):
    return message_database[message_id - 1]


@router.post("/", response_model=MessageInDB)
async def create_message(message: Message):
    message_db = MessageInDB(user_id=message.user_id,
                             chat_id=message.chat_id,
                             text=message.text,
                             created_date=message.created_date)
    return message_db


@router.put("/{message_id}", response_model=MessageInDB)
async def update_message(message_id: int, message: Message):
    message_db = message_database[message_id - 1]
    for param, value in message.dict().items():
        message_db[param] = value
    return message_db


@router.delete("/{message_id}")
async def delete_message(message_id: int):
    db = list(message_database)
    del db[message_id - 1]
