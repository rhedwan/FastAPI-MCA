import uuid
from fastapi import HTTPException, status
from sqlmodel import Session
from schemas import PostCreate, PostRead, PostUpdate
from models import Post, User



def get_post_or_404(post_id:uuid.UUID, session: Session) -> Post:
    post = session.get(Post, post_id)
    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Post not found"
        )
    
    return post

def require_post_author(post: Post, user: User) -> None:
    if post.author_id != user.id and not user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to change this post"
        )


def create_post(data: PostCreate, user: User, session: Session) -> Post:
    post = Post(**data.model_dump(), author_id=user.id)
    session.add(post)
    session.commit()
    session.refresh(post)
    return post