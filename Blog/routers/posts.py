from fastapi import APIRouter, status, HTTPException, Query, Response
from schemas import PostRead, PostCreate, PublishedPost, PostUpdate
from dependencies import CurrentUser, DatabaseSession
from services.posts import create_post, get_post_or_404, require_post_author, update_post, list_published_posts, delete_post
from typing import Annotated
from sqlmodel import col, select
import uuid
from models import Post
router = APIRouter()


@router.post("", response_model=PostRead, status_code=status.HTTP_201_CREATED)
def create(data:PostCreate, current_user:CurrentUser, session: DatabaseSession):
    return create_post(data, current_user, session)



@router.get("", response_model=list[PostRead])
def list_posts(
    session: DatabaseSession, 
    search: str | None = None,
    limit: Annotated[int, Query(ge=1, le=100)] = 20,
    offset: Annotated[int, Query(ge=0)] =0,
):
    return list_published_posts(session, search, limit, offset)


@router.get("/mine", response_model=list[PostRead])
def list_my_posts(
    current_user: CurrentUser,  session: DatabaseSession
):
    statement = (
        select(Post)
        .where(Post.author_id == current_user.id)
        .order_by(col(Post.created_at).desc())
    )

    return session.exec(statement).all()

@router.get("/{post_id}", response_model=PostRead)
def read_post(post_id:uuid.UUID, session: DatabaseSession):
    post = get_post_or_404(post_id, session)
    if not post.is_published:
        raise HTTPException(
            status_code=404, detail="Post not found"
        )
    return post


@router.patch("/{post_id}", response_model=PostRead)
def update(post_id:uuid.UUID, data:PostUpdate, current_user: CurrentUser,  session: DatabaseSession):
    return update_post(post_id, data, current_user, session)


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(post_id:uuid.UUID, current_user: CurrentUser,  session: DatabaseSession):
    delete_post(post_id, current_user, session)
    return Response(status_code=status.HTTP_204_NO_CONTENT)