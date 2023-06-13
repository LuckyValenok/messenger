from fastapi import APIRouter, Depends

from core.db.models import User
from crud.chat import get_chat_by_id, create_chat as crud_create_chat, delete_chat_by_id, change_name_chat_by_id
from deps import get_current_user
from exceptions.validation import UserDontHavePermissionsException
from schemas.chat import Chat, ChatOutScheme, ChatWithMessagesOutScheme, ChatWithLastMessageOutScheme

router = APIRouter(prefix="/chat")


@router.get("/get/{chat_id}", response_model=ChatWithMessagesOutScheme)
async def get_chat(chat_id: int, user: User = Depends(get_current_user)):
    chat = get_chat_by_id(chat_id)
    if user not in chat.users:
        raise UserDontHavePermissionsException
    return chat


@router.post("/new", response_model=ChatOutScheme)
async def create_chat(chat: Chat, user: User = Depends(get_current_user)):
    return crud_create_chat(chat, user)


@router.put("/change_name/{chat_id}")
async def change_name_chat(chat_id: int, new_name: str, user: User = Depends(get_current_user)):
    chat = get_chat_by_id(chat_id)
    if user not in chat.users:
        raise UserDontHavePermissionsException
    return change_name_chat_by_id(chat_id, new_name)


@router.delete("/delete/{chat_id}")
async def delete_chat(chat_id: int, user: User = Depends(get_current_user)):
    chat = get_chat_by_id(chat_id)
    if user not in chat.users:
        raise UserDontHavePermissionsException
    return delete_chat_by_id(chat_id)


@router.get("/me")
async def get_chat_by_user(user: User = Depends(get_current_user)):
    return_list = []
    chats = user.chats
    for chat in chats:
        if len(chat.messages):
            return_list.append(
                ChatWithLastMessageOutScheme(id=chat.id, name=chat.name, type=chat.type, created_date=chat.created_date,
                                             removed=chat.removed, message=chat.messages[-1]))
        else:
            return_list.append(ChatOutScheme(id=chat.id, name=chat.name, type=chat.type, created_date=chat.created_date,
                                             removed=chat.removed))
    return return_list
