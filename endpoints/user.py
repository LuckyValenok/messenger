from fastapi import APIRouter

from crud.user import get_user_by_id as crud_get_user_by_id, \
    get_users, create_user, change_name as crud_change_name

from schemas.user import User


router = APIRouter(prefix="/user")


@router.get("/{user_id}")
async def get_user_by_id(user_id: int):
    return crud_get_user_by_id(user_id)


@router.get("/list")
async def get_users():
    return get_users()


@router.post("/new", response_model=User)
async def create_user(user: User):
    return create_user(user)


@router.put("/change_name/{user_id}")
async def change_name(user_id: int, new_name: str):
    return crud_change_name(user_id, new_name)

