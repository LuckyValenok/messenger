from fastapi import APIRouter

from crud.user import get_users, create_user, change_name as crud_change_name
from schemas.user import User


router = APIRouter(prefix="/user")


@router.get("/list")
async def get_users():
    return get_users()


@router.post("/new", response_model=User)
async def create_user(user: User):
    return create_user(user)


@router.put("/change_name/{user_id}")
async def change_name(user_id: int, new_name: str):
    return crud_change_name(user_id, new_name)

