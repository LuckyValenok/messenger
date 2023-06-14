from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from core.db.models import User
from core.db.session import session_maker
from crud.user import get_user_by_id
from exceptions.validation import InvalidTokenException
from security import get_user_from_jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login/")


def get_db() -> Session:
    db = session_maker()
    try:
        yield db
    finally:
        db.close()


async def get_current_user_id(token: str = Depends(oauth2_scheme)) -> int:
    user_id = get_user_from_jwt(token)
    if user_id is None:
        raise InvalidTokenException
    return user_id


async def get_current_user(session: Session = Depends(get_db), user_id: int = Depends(get_current_user_id)) -> User:
    return get_user_by_id(session, user_id)
