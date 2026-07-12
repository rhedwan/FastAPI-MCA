import uuid
from pydantic import BaseModel, EmailStr
from sqlmodel import SQLModel, Field



class UserCreate(SQLModel):
    username: str = Field(min_length=3)
    email: EmailStr
    password: str = Field(min_length=6)



class UserRead(SQLModel):
    id: uuid.UUID
    username: str 
    email: EmailStr
    is_admin: bool


