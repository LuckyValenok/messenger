from fastapi import WebSocket, WebSocketDisconnect, APIRouter

from crud.chat import get_chat_by_id
from crud.user import get_user_by_id
from deps import get_current_user
from exceptions.validation import UserDontHavePermissionsException

router = APIRouter(prefix="/ws")


class ConnectionManager:
    def __init__(self):
        self.active_connection_for_user = {}
        self.active_connections_for_chats = {}

    async def connect(self, websocket: WebSocket, user=None, chat=None):
        await websocket.accept()
        if user:
            self.active_connection_for_user[user.id] = websocket
        if chat:
            if chat.id in self.active_connections_for_chats:
                self.active_connections_for_chats[chat.id].append(websocket)
            else:
                self.active_connections_for_chats[chat.id] = [websocket]

    def disconnect(self, websocket: WebSocket):
        self.active_connection_for_user = {k: v for k, v in self.active_connection_for_user.items() if v == websocket}
        for k, v in self.active_connection_for_user.items():
            if websocket in v:
                v.remove(websocket)

    async def broadcast(self, message: str, user_id=None, chat_id=None):
        if user_id:
            await self.active_connection_for_user[user_id].send_text(message)
        if chat_id:
            for connection in self.active_connections_for_chats[chat_id]:
                await connection.send_text(message)


manager = ConnectionManager()


@router.websocket("/chat/{chat_id}")
async def websocket_endpoint(websocket: WebSocket, chat_id: int, token: str):
    user_id = await get_current_user(token)
    user = get_user_by_id(user_id)
    chat = get_chat_by_id(chat_id)
    if user not in chat.users:
        raise UserDontHavePermissionsException
    await manager.connect(websocket, chat=chat)
    try:
        while True:
            await websocket.receive()
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        print('disconnect')
