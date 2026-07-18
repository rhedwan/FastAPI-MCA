from fastapi import APIRouter, Depends
from typing import Annotated
from sqlmodel import Session
from database import get_db

DatabaseSession = Annotated[Session, Depends(get_db)]

router = APIRouter()



@router.post("/register")
def register():
    pass



@router.post("/login")
def login():
    pass