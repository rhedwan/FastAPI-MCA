import uuid
from fastapi import HTTPException, status
from sqlmodel import Session, select
from models import Comment, Post, User
from schemas import CommentCreate, CommmentUpdate
from services.posts import get_post_or_404

def get_comment_or_404(post_id:uuid.UUID, session: Session) -> Comment:
    comment = session.get(Comment, post_id)
    if comment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Comment not found"
        )
    
    return comment


def create_comment(post_id:uuid.UUID, data: CommentCreate, user: User, session: Session) -> Comment:
    post = get_post_or_404(post_id, session)
    if not post.is_published:
        raise HTTPException(
            status_code=404, detail= "Post not found"
        )

    comment = Comment(
        content=data.content,
        post_id=post.id,
        author_id=user.id
    )

    session.add(comment)
    session.commit()
    session.refresh(comment)
    return comment



def update_comment(
        comment_id: uuid.UUID, data: CommmentUpdate, 
        user: User, session: Session
    ):

    comment = get_comment_or_404(comment_id, session)
    if comment.author_id != user.id: 
        raise HTTPException(
         status_code=403, detail= "Not Allowed"
        )

    comment.content = data.content
    session.add(comment)
    session.commit()
    session.refresh(comment)
    return comment
    
    


def delete_comment(
        comment_id: uuid.UUID,
        user: User, session: Session
    ):

    comment = get_comment_or_404(comment_id, session)
    if comment.author_id != user.id and not user.is_admin: 
        raise HTTPException(
         status_code=403, detail= "Not Allowed"
        )

    session.delete(comment)
    session.commit()