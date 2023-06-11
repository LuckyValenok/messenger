from fastapi import APIRouter, Depends, HTTPException, status

from core.db.models import User
from core.db.session import get_session
from schemas.user import User as UserSchema
from security import get_password_hash, verify_password


def get_users():
    return get_session().query(User).filter(User.deleted == False).all()


def get_user_by_id(user_id: int) -> User:
    user = get_session().query(User).filter((User.id == user_id) & (User.deleted == False)).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)
    return user


def get_user_by_login(login: str):
    user = get_session().query(User).filter(User.login == login).one_or_none()
    if user is None:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)
    return user


def create_user(user: UserSchema) -> User:
    try:
        hashed_password = get_password_hash(user.password)
        new_user = User(name=user.name, login=user.login, password=hashed_password)
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


def authenticate(login: str, password: str):
    user = get_user_by_login(login)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user
