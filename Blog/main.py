from fastapi import FastAPI
from routers import auth, users

app = FastAPI(title="Blog API")


app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/user", tags=["Users"])