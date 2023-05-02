from core.db.models import User
from core.db.session import get_session
from schemas.user import User as UserSchema


def get_users() -> dict:
    return get_session().query(User).all()


def get_user_by_id(user_id: int) -> User:
    return get_session().query(User).filter_by(id=user_id).first()


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
