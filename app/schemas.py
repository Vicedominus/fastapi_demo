from datetime import datetime
from lib2to3.pgen2 import token
from typing import Optional
from pydantic import BaseModel, EmailStr

from pydantic.types import conint

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

class PostBase(BaseModel):
    title: str
    content: str
    public: bool = True

class CreatePost(PostBase):
    pass

class UpdatePost(PostBase):
    public: bool

class PostResponse(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserResponse

    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post: PostResponse
    votes: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: EmailStr
    password: str

class CreateUser(UserBase):
    pass



class UserLogin(UserBase):
    pass


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)