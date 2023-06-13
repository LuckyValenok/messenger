from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from core.db.session import session
from crud.user import get_user_by_id
from exceptions.validation import InvalidTokenException
from security import get_user_from_jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login/")


def get_db():
    db = session()
    try:
        yield db
    except:
        db.close()


async def get_current_user_id(token: str = Depends(oauth2_scheme)):
    user_id = get_user_from_jwt(token)
    if user_id is None:
        raise InvalidTokenException
    return user_id


async def get_current_user(user_id: int = Depends(get_current_user_id)):
    return get_user_by_id(user_id)
