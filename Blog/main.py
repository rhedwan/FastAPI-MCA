from fastapi import FastAPI
from routers import auth, posts, comments
from config import CORS_ORIGINS
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(title="Blog API")

if CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=CORS_ORIGINS,
        allow_credentials=True, 
        allow_methods=["*"],
        allow_headers=["*"]
    )

@app.get("/", tags=["General"])
def home():
    return {"status": "ok, server is running!"}


app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(posts.router, prefix="/post", tags=["Post"])
app.include_router(comments.router, prefix="/comment", tags=["Comment"])
