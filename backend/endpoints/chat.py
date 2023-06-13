from fastapi import APIRouter, HTTPException, status, Depends

from crud.chat import get_chat_by_id, create_chat as crud_create_chat, delete_chat_by_id, change_name_chat_by_id, \
    get_chats as crud_get_chats
from crud.user import get_user_by_id
from deps import get_current_user
from schemas.chat import Chat, ChatOutScheme, ChatWithMessagesOutScheme

router = APIRouter(prefix="/chat")


@router.get("/list")
async def get_chats():
    chats = crud_get_chats()
    if chats is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return chats


@router.get("/get/{chat_id}", response_model=ChatWithMessagesOutScheme)
async def get_chat(chat_id: int):
    chat_id = get_chat_by_id(chat_id)
    if chat_id is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return chat_id


@router.post("/new", response_model=Chat)
async def create_chat(chat: Chat):
    return crud_create_chat(chat)


@router.put("/change_name/{chat_id}")
async def change_name_chat(chat_id: int, new_name: str):
    return change_name_chat_by_id(chat_id, new_name)


@router.delete("/delete/{chat_id}", response_model=Chat)
async def delete_chat(chat_id: int):
    chat_id = delete_chat_by_id(chat_id)
    if chat_id is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return chat_id


@router.get("/me", response_model=list[ChatOutScheme])
async def get_chat_by_user(user_id: int = Depends(get_current_user)):
    return get_user_by_id(user_id).chats
