from typing import List
from pydantic import BaseModel

class CreateBlog(BaseModel):
    title: str
    body: str
    user_id: int = 1
    class Config():
            orm_mode = True

class User(BaseModel):
    name: str
    email: str
    password: str
class ShowUser(BaseModel):
        name: str
        email: str
        blogs: List[CreateBlog]
        class Config():
            orm_mode = True


class ShowBlog(BaseModel):
    title: str
    body: str
    writer: ShowUser
    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None