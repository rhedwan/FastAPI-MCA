import uuid
from datetime import datetime, timezone
from sqlmodel import SQLModel, Field, Relationship



def utc_now() -> datetime:
    return datetime.now(timezone.utc)



class User(SQLModel, table=True):

    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True
    )

    username: str = Field(index=True, unique=True)
    email: str = Field(index=True, unique=True)

    hashed_password: str

    is_active: bool = True
    is_admin: bool = False


    created_at: datetime = Field(
        default_factory=utc_now
    )


    updated_at: datetime = Field(
        default_factory=utc_now,
        sa_column_kwargs={
            "onupdate": utc_now,
        }
    )

    posts: list["Post"] = Relationship(
        back_populates="author",
        cascade_delete=True,
    )

    comments: list["Comment"] = Relationship(
        back_populates="author",
        cascade_delete=True,
    )


class Post(SQLModel, table=True):

    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True
    )
    title: str = Field(
        index=True, 
        min_length=3, 
        max_length=200
    )
    content: str = Field(min_length=10)


    created_at: datetime = Field(
        default_factory=utc_now
    )

    updated_at: datetime = Field(
        default_factory=utc_now,
        sa_column_kwargs={
            "onupdate": utc_now,
        }
    )

    author_id: uuid.UUID = Field(
        foreign_key="user.id"
    )

    author: User = Relationship(back_populates="posts")
    comments: list["Comment"] = Relationship(
        back_populates="post",
        cascade_delete=True,
    )



class Comment(SQLModel, table=True):

    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True
    )
    content: str = Field(min_length=1, max_length=1000)


    created_at: datetime = Field(
        default_factory=utc_now
    )

    updated_at: datetime = Field(
        default_factory=utc_now,
        sa_column_kwargs={
            "onupdate": utc_now,
        }
    )

    author_id: uuid.UUID = Field(
        foreign_key="user.id", index=True
    )
    post_id: uuid.UUID = Field(
        foreign_key="post.id", index=True
    )
    author: User = Relationship(back_populates="comments")
    post: Post = Relationship(back_populates="comments")

