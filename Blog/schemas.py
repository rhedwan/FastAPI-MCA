import uuid
from pydantic import BaseModel, EmailStr
from sqlmodel import SQLModel, Field



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


class TokenResponse(SQLModel):
    access_token: str
    token_type: str = "bearer"


