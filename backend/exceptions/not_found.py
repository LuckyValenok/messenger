from fastapi import HTTPException
from starlette import status


class UserNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_204_NO_CONTENT)
