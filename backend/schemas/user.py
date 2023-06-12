from pydantic import BaseModel


class User(BaseModel):
    login: str
    password: str
    name: str

    class Config:
        orm_mode = True


class UserWithoutPassword(BaseModel):
    id: int
    login: str
    name: str
    deleted: bool

    class Config:
        orm_mode = True
