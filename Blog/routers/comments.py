from fastapi import APIRouter, status, HTTPException, Query, Response
from schemas import CommentRead, CommentCreate, CommmentUpdate
from dependencies import CurrentUser, DatabaseSession
from services.comments import create_comment, update_comment, delete_comment
from sqlmodel import col, select
import uuid
from models import Comment, Post
router = APIRouter()


@router.post(
    "/{post_id}", 
    response_model= CommentRead,
    status_code=status.HTTP_201_CREATED
)
def create(
    post_id:uuid.UUID, data:CommentCreate, 
    current_user: CurrentUser,  
    session: DatabaseSession
    ):

    return create_comment(post_id, data, current_user, session)


@router.get(
        "/{post_id}", response_model= list[CommentRead]
    )
def list_comment(post_id:uuid.UUID, session: DatabaseSession):
    post = session.get(Post, post_id)
    if post is None or not post.is_published:
        raise HTTPException(
            status_code=403, detail= "Not Allowed"
        )

    return session.exec(
        select(Comment).where(Comment.post_id == post_id)
    ).all()


@router.patch("/{comment_id}", response_model=CommentRead)
def update(
    comment_id:uuid.UUID, data:CommmentUpdate,
    current_user: CurrentUser,  session: DatabaseSession
    ):
    return update_comment(comment_id, data, current_user, session)


@router.delete("/{comment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(comment_id:uuid.UUID, current_user: CurrentUser,  session: DatabaseSession):
    delete_comment(comment_id, current_user, session)
    return Response(status_code=status.HTTP_204_NO_CONTENT)