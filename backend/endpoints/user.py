from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.user import get_user_by_id as crud_get_user_by_id, \
    get_users as crud_get_users, create_user as crud_create_user, change_name as crud_change_name, \
    delete_user as crud_delete_user
from deps import get_current_user, get_db

from schemas.user import User, UserWithoutPassword, NewName

router = APIRouter(prefix="/user")


@router.get("/list", response_model=list[UserWithoutPassword], dependencies=[Depends(get_current_user)])
async def get_users(session: Session = Depends(get_db)):
    return crud_get_users(session)


@router.get("/get/{user_id}", response_model=UserWithoutPassword, dependencies=[Depends(get_current_user)])
async def get_user_by_id(user_id: int, session: Session = Depends(get_db)) -> User:
    return crud_get_user_by_id(session, user_id)


@router.post("/new", response_model=User)
async def create_user(user: User, session: Session = Depends(get_db)):
    return crud_create_user(session, user)


@router.put("/change_name")
async def change_name(model: NewName, session: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return crud_change_name(session, user, model.new_name)


@router.delete("/delete", response_model=User)
async def delete_user(session: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return crud_delete_user(session, user)


@router.get("/me", response_model=UserWithoutPassword)
async def get_user_by_id(user: User = Depends(get_current_user)):
    return user
