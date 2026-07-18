from fastapi import APIRouter, Depends, status
from typing import Annotated
from sqlmodel import Session
from database import get_db
from schemas import UserRead, UserCreate, TokenResponse, LoginRequest
from services.auth import authenticate_user, register_user
from security import create_access_token
from dependencies import CurrentUser


DatabaseSession = Annotated[Session, Depends(get_db)]

router = APIRouter()



@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def register(data: UserCreate, session: DatabaseSession):
    return register_user(data, session)
    

@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, session: DatabaseSession):
    user = authenticate_user(data, session)
    return TokenResponse(access_token=create_access_token(user.id))


@router.get("/me", response_model=UserRead)
def login(current_user: CurrentUser):
    return current_user