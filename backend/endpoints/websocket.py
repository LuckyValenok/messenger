from fastapi import WebSocket, APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.websockets import WebSocketState

from crud.chat import get_chat_by_id
from crud.user import get_user_by_id
from deps import get_current_user_id, get_db
from exceptions.validation import UserDontHavePermissionsException

router = APIRouter(prefix="/ws")


class ConnectionManager:
    def __init__(self):
        self.active_connection_for_user = {}
        self.active_connections_for_chats = {}

    async def connect(self, websocket: WebSocket, user_id=None, chat_id=None):
        await websocket.accept()
        if user_id:
            self.active_connection_for_user[user_id] = websocket
        if chat_id:
            if chat_id in self.active_connections_for_chats:
                self.active_connections_for_chats[chat_id].append(websocket)
            else:
                self.active_connections_for_chats[chat_id] = [websocket]

    def disconnect(self, websocket: WebSocket, from_user=False, from_chats=False):
        if from_user:
            self.active_connection_for_user = {k: v for k, v in self.active_connection_for_user.items() if v == websocket}
        if from_chats:
            for _, v in self.active_connections_for_chats.items():
                if websocket in v:
                    v.remove(websocket)

    async def broadcast(self, message, user_id=None, chat_id=None):
        try:
            if user_id and user_id in self.active_connection_for_user:
                await self.active_connection_for_user[user_id].send_text(message)
            if chat_id:
                for connection in self.active_connections_for_chats[chat_id]:
                    await connection.send_text(message)
        except RuntimeError:
            pass


manager = ConnectionManager()


@router.websocket("/chat/{chat_id}")
async def websocket_endpoint(websocket: WebSocket, chat_id: int, token: str, session: Session = Depends(get_db)):
    user_id = await get_current_user_id(token)
    user = get_user_by_id(session, user_id)
    chat = get_chat_by_id(session, chat_id)
    if user not in chat.users:
        raise UserDontHavePermissionsException
    await manager.connect(websocket, chat_id=chat_id)
    while websocket.client_state == WebSocketState.CONNECTED:
        await websocket.receive()
    manager.disconnect(websocket, from_chats=True)


@router.websocket("/user")
async def websocket_endpoint(websocket: WebSocket, token: str, session: Session = Depends(get_db)):
    user_id = await get_current_user_id(token)
    user = get_user_by_id(session, user_id)
    await manager.connect(websocket, user_id=user.id)
    while websocket.client_state == WebSocketState.CONNECTED:
        await websocket.receive()
    manager.disconnect(websocket, from_user=True)
