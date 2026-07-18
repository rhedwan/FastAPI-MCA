from fastapi import HTTPException, status
from sqlmodel import Session, select

from models import User
from schemas import LoginRequest, UserCreate
from security import hash_password, verify_password



def get_user_by_email(email:str, session:Session) -> User | None: 
    return session.exec(select(User).where(User.email == email)).first()


def register_user(data: UserCreate, session: Session) -> User: 
    email_exists = get_user_by_email(data.email, session)
    username_exist =  session.exec(select(User).where(User.username == data.username)).first()

    if email_exists:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email is already registered"
        )
    
    if username_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username is already taken"
        )
    
    user = User(
        username=data.username,
        email=data.email,
        hashed_password=hash_password(data.password)
    )

    session.add(user)
    session.commit()
    session.refresh(user)
    return user



def authenticate_user(data: LoginRequest, session:Session) -> User:
    user = get_user_by_email(data.email, session)
    if user is None or not verify_password(data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )
    
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User account is inactive"
        )
    
    return user


