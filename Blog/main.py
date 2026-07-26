from fastapi import FastAPI
from routers import auth, posts, comments

app = FastAPI(title="Blog API")


app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(posts.router, prefix="/post", tags=["Post"])
app.include_router(comments.router, prefix="/comment", tags=["Comment"])
