import uuid
from pydantic import BaseModel, EmailStr
from sqlmodel import SQLModel, Field
from datetime import datetime



class UserCreate(SQLModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(min_length=8, max_length=120)


class LoginRequest(SQLModel):
    email: EmailStr
    password: str


class UserUpdate(SQLModel):
    username: str | None = Field( default = None, min_length=3, max_length=50)
    email: EmailStr | None = None



class UserRead(SQLModel):
    id: uuid.UUID
    username: str 
    email: EmailStr
    is_admin: bool
    created_at: datetime


class TokenResponse(SQLModel):
    access_token: str
    token_type: str = "bearer"



class PostCreate(SQLModel):
    title: str = Field(min_length=3, max_length=200)
    content: str = Field(min_length=1)
    is_published: bool = False

class PostUpdate(SQLModel):
    title: str | None = Field(default=None, min_length=3, max_length=200)
    content: str | None = Field(default=None, min_length=1)


class PublishedPost(SQLModel):
    is_published: bool


class PostRead(SQLModel):
    id: uuid.UUID
    title: str
    content: str
    is_published: bool
    created_at: datetime
    updated_at: datetime



class CommentCreate(SQLModel):
    content: str = Field(min_length=3, max_length=1000)

class CommmentUpdate(SQLModel):
    content: str = Field(min_length=3, max_length=1000)


class CommentRead(SQLModel):
    id: uuid.UUID
    content: str
    author_id: uuid.UUID
    post_id: uuid.UUID
    created_at: datetime
    updated_at: datetime