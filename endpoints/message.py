from fastapi import APIRouter

router = APIRouter(prefix="/message")


@router.get("/{chat_id}")
async def get_messages_in_chat(chat_id: int):
    return
