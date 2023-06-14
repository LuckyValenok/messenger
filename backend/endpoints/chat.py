from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.db.models import User
from crud.chat import get_chat_by_id, create_chat as crud_create_chat, delete_chat_by_id, change_name_chat_by_id, \
    add_member as crud_add_member
from crud.user import get_user_by_login
from deps import get_current_user, get_db
from endpoints.websocket import manager
from exceptions.validation import UserDontHavePermissionsException
from schemas.chat import Chat, ChatOutScheme, ChatWithMessagesOutScheme, ChatWithLastMessageOutScheme

router = APIRouter(prefix="/chat")


@router.get("/get/{chat_id}", response_model=ChatWithMessagesOutScheme)
async def get_chat(chat_id: int, session: Session = Depends(get_db), user: User = Depends(get_current_user)):
    chat = get_chat_by_id(session, chat_id)
    if user not in chat.users:
        raise UserDontHavePermissionsException
    return chat


@router.post("/new", response_model=ChatOutScheme)
async def create_chat(chat_scheme: Chat, session: Session = Depends(get_db), user: User = Depends(get_current_user)):
    chat = crud_create_chat(session, chat_scheme, user)
    try:
        return chat
    finally:
        await manager.broadcast(ChatOutScheme(**chat.__dict__).json(), user_id=user.id)


@router.put("/change_name/{chat_id}")
async def change_name_chat(chat_id: int, new_name: str, session: Session = Depends(get_db),
                           user: User = Depends(get_current_user)):
    chat = get_chat_by_id(session, chat_id)
    if user not in chat.users:
        raise UserDontHavePermissionsException
    return change_name_chat_by_id(session, chat_id, new_name)


@router.post("/add_member/{chat_id}")
async def add_member(chat_id: int, username: str, session: Session = Depends(get_db),
                     user: User = Depends(get_current_user)):
    chat = get_chat_by_id(session, chat_id)
    if user not in chat.users:
        raise UserDontHavePermissionsException
    member = get_user_by_login(session, username)
    try:
        return crud_add_member(session, chat, member)
    finally:
        if chat.messages:
            scheme = ChatWithLastMessageOutScheme(**chat.__dict__, message=chat.messages[-1]).json()
        else:
            scheme = ChatOutScheme(**chat.__dict__).json()
        await manager.broadcast(scheme, user_id=member.id)


@router.delete("/delete/{chat_id}")
async def delete_chat(chat_id: int, session: Session = Depends(get_db), user: User = Depends(get_current_user)):
    chat = get_chat_by_id(session, chat_id)
    if user not in chat.users:
        raise UserDontHavePermissionsException
    return delete_chat_by_id(session, chat_id)


@router.get("/me")
async def get_chat_by_user(user: User = Depends(get_current_user)):
    return_list = []
    chats = user.chats
    for chat in chats:
        if len(chat.messages):
            return_list.append(
                ChatWithLastMessageOutScheme(**chat.__dict__, message=chat.messages[-1]))
        else:
            return_list.append(ChatOutScheme(**chat.__dict__))
    return return_list
