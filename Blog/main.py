from fastapi import FastAPI
from routers import auth, posts

app = FastAPI(title="Blog API")


app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(posts.router, prefix="/post", tags=["Post"])