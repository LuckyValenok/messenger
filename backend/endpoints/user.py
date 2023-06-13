from fastapi import APIRouter, Depends

from crud.user import get_user_by_id as crud_get_user_by_id, \
    get_users as crud_get_users, create_user as crud_create_user, change_name as crud_change_name, \
    delete_user as crud_delete_user
from deps import get_current_user

from schemas.user import User, UserWithoutPassword

router = APIRouter(prefix="/user")


@router.get("/list", response_model=list[UserWithoutPassword], dependencies=[Depends(get_current_user)])
async def get_users():
    return crud_get_users()


@router.get("/get/{user_id}", response_model=UserWithoutPassword, dependencies=[Depends(get_current_user)])
async def get_user_by_id(user_id: int) -> User:
    return crud_get_user_by_id(user_id)


@router.post("/new", response_model=User)
async def create_user(user: User):
    return crud_create_user(user)


@router.put("/change_name")
async def change_name(new_name: str, user: User = Depends(get_current_user)):
    return crud_change_name(user, new_name)


@router.delete("/delete", response_model=User)
async def delete_user(user: User = Depends(get_current_user)):
    return crud_delete_user(user)


@router.get("/me", response_model=UserWithoutPassword)
async def get_user_by_id(user: User = Depends(get_current_user)):
    return user
