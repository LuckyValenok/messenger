from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from crud.user import authenticate
from deps import get_db
from exceptions.validation import IncorrectPasswordException
from security import create_access_token

router = APIRouter(prefix="/login")


@router.post("/")
async def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
        session: Session = Depends(get_db)
):
    user = authenticate(session, form_data.username, form_data.password)
    if not user:
        raise IncorrectPasswordException

    access_token = create_access_token(user_id=user.id)
    return {"access_token": access_token, "token_type": "bearer"}
