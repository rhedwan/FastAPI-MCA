import uuid
from fastapi import HTTPException, status
from sqlmodel import Session
from schemas import PostCreate, PostRead, PostUpdate
from models import Post, User
from sqlmodel import col, select, or_



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

def list_published_posts(
        session: Session,  search: str, 
        limit:int, offset:int) -> list[Post]:

    statement = select(Post).where(Post.is_published).order_by(col(Post.created_at).desc())

    if search:
        statement = statement.where(
            or_(
                col(Post.title).contains(search),
                col(Post.content).contains(search)
            )
        )


    statement = statement.offset(offset).limit(limit)
    return session.exec(statement).all()

def update_post(post_id:uuid.UUID, data: PostUpdate, user: User, session: Session) -> Post:
    post = get_post_or_404(post_id, session)
    require_post_author(post, user)
    post.sqlmodel_update(data.model_dump(exclude_unset=True))
    session.add(post)
    session.commit()
    session.refresh(post)
    return post
