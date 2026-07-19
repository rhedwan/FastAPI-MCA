from fastapi import APIRouter, status, HTTPException
from schemas import PostRead, PostCreate, PublishedPost
from dependencies import CurrentUser, DatabaseSession
from services.posts import create_post, get_post_or_404, require_post_author

import uuid
router = APIRouter()


@router.post("", response_model=PostRead, status_code=status.HTTP_201_CREATED)
def create(data:PostCreate, current_user:CurrentUser, session: DatabaseSession):
    return create_post(data, current_user, session)


@router.get("/{post_id}", response_model=PostRead)
def read_post(post_id:uuid.UUID, session: DatabaseSession):
    post = get_post_or_404(post_id, session)
    if not post.is_published:
        raise HTTPException(
            status_code=404, detail="Post not found"
        )
    return post


@router.patch("/{post_id}/publish", response_model=PostRead)
def publish(post_id:uuid.UUID, data:PublishedPost, current_user: CurrentUser,  session: DatabaseSession):
    post = get_post_or_404(post_id, session)
    require_post_author(post, current_user)
    post.is_published = data.is_published
    session.add(post)
    session.commit()
    session.refresh(post)
    return post