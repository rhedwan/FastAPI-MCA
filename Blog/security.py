import os
import uuid
from datetime import datetime, timedelta, timezone

import jwt
from pwdlib import PasswordHash


SECRET_KEY = "ZCkgPSrTc0207rcXPmh8mlGEEnl1KYjiSxeOzOGk3dvh95cU"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MOINUTES = 30



password_hash = PasswordHash.recommended()


def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(plain_password: str, hash_password: str) -> bool:
    return password_hash.verify(plain_password, hash_password)


def create_access_token(user_id: uuid.UUID) -> str:
    expires_at =  datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MOINUTES)
    payload = {
        "sub": str(user_id), 
        "exp": expires_at
    }

    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
 
def decode_access_token(token:str) -> str:
   payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
   return uuid.UUID(payload['sub'])
 