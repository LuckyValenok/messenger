from pydantic import BaseModel


class User(BaseModel):
    login: str
    password: str
    name: str

    class Config:
        orm_mode = True
