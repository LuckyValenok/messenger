from fastapi import HTTPException

from core.db.models import User
from core.db.session import get_session
from schemas.user import User as UserSchema


def get_users():
    return get_session().query(User).filter(User.deleted == False).all()


def get_user_by_id(user_id: int) -> User:
    user = get_session().query(User).filter((User.id == user_id) & (User.deleted == False)).first()
    if user is None:
        raise HTTPException(204)
    return user


def create_user(user: UserSchema) -> User:
    try:
        new_user = User(name=user.name, login=user.login, password=user.password)
        get_session().add(new_user)
        return new_user
    finally:
        get_session().commit()


def change_name(user_id: int, new_name: str) -> str:
    try:
        user = get_user_by_id(user_id)
        prev_name = user.name
        user.name = new_name
        return prev_name
    finally:
        get_session().commit()


def delete_user_by_id(user_id: int) -> User:
    try:
        user = get_user_by_id(user_id)
        user.deleted = True
        return user
    finally:
        get_session().commit()
