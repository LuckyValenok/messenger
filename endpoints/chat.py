from fastapi import APIRouter

from crud.chat import get_chat_by_id, create_new_chat, delete_chat_by_id, change_name_chat_by_id, get_chats
from schemas.chat import Chat

router = APIRouter(prefix="/chat")


@router.get("/list")
async def list_chats():
    return get_chats()


@router.get("/get/{chat_id}")
async def get_chat(chat_id: int):
    return get_chat_by_id(chat_id)


@router.post("/new", response_model=Chat)
async def create_chat(chat: Chat):
    return create_new_chat(chat)


@router.put("/change_name/{chat_id}")
async def change_name_chat(chat_id: int, new_name: str):
    return change_name_chat_by_id(chat_id, new_name)


@router.delete("/delete/{chat_id}")
async def delete_chat(chat_id: int):
    return delete_chat_by_id(chat_id)
