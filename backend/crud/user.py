from sqlalchemy.orm import Session

from core.db.models import User
from exceptions.not_found import UserNotFoundException
from exceptions.validation import IncorrectPasswordException, LoginAlreadyInUseException
from schemas.user import User as UserSchema
from security import get_password_hash, verify_password


def get_users(session: Session):
    return session.query(User).filter(User.deleted == False).all()


def get_user_by_id(session: Session, user_id: int) -> User:
    user = session.query(User).filter((User.id == user_id) & (User.deleted == False)).first()
    if user is None:
        raise UserNotFoundException
    return user


def get_user_by_login(session: Session, login: str):
    user = session.query(User).filter(User.login == login).one_or_none()
    if user is None:
        raise UserNotFoundException
    return user


def create_user(session: Session, user_schema: UserSchema) -> User:
    try:
        user = get_user_by_login(session, user_schema.login)
        if user is not None:
            raise LoginAlreadyInUseException
    except UserNotFoundException:
        pass
    hashed_password = get_password_hash(user_schema.password)
    new_user = User(name=user_schema.name, login=user_schema.login, password=hashed_password)
    session.add(new_user)
    session.commit()
    return new_user


def change_name(session: Session, user: User, new_name: str) -> str:
    prev_name = user.name
    user.name = new_name
    session.commit()
    return prev_name


def delete_user(session: Session, user: User) -> User:
    user.deleted = True
    session.commit()
    return user


def authenticate(session: Session, login: str, password: str):
    user = get_user_by_login(session, login)
    if not verify_password(password, user.password):
        raise IncorrectPasswordException
    return user
