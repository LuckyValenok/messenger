from core.db.models import User
from core.db.session import get_session
from exceptions.not_found import UserNotFoundException
from exceptions.validation import IncorrectPasswordException, LoginAlreadyInUseException
from schemas.user import User as UserSchema
from security import get_password_hash, verify_password


def get_users():
    return get_session().query(User).filter(User.deleted == False).all()


def get_user_by_id(user_id: int) -> User:
    user = get_session().query(User).filter((User.id == user_id) & (User.deleted == False)).first()
    if user is None:
        raise UserNotFoundException
    return user


def get_user_by_login(login: str):
    user = get_session().query(User).filter(User.login == login).one_or_none()
    if user is None:
        raise UserNotFoundException
    return user


def create_user(user_schema: UserSchema) -> User:
    try:
        user = get_user_by_login(user_schema.login)
        if user is not None:
            raise LoginAlreadyInUseException
    except UserNotFoundException:
        pass
    try:
        hashed_password = get_password_hash(user_schema.password)
        new_user = User(name=user_schema.name, login=user_schema.login, password=hashed_password)
        get_session().add(new_user)
        return new_user
    finally:
        get_session().commit()


def change_name(user: User, new_name: str) -> str:
    try:
        prev_name = user.name
        user.name = new_name
        return prev_name
    finally:
        get_session().commit()


def delete_user(user: User) -> User:
    try:
        user.deleted = True
        return user
    finally:
        get_session().commit()


def authenticate(login: str, password: str):
    user = get_user_by_login(login)
    if not verify_password(password, user.password):
        raise IncorrectPasswordException
    return user
