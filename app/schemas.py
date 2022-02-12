from datetime import datetime
from pydantic import BaseModel, EmailStr, conint
from typing import Optional

from app.models import User


class PostBase (BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(UserCreate):
    pass


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)


# This is for response model
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class PostResponse(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserResponse

    class Config:
        orm_mode = True


class PostResult (BaseModel):
    Post: PostResponse
    votes: int


class TokenResponse(BaseModel):

    access_token: str
    token_type: str

    class Config:
        orm_mode = True


class TokenData(BaseModel):
    id: Optional[str] = None
