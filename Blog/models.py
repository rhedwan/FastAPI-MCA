import uuid
from datetime import datetime, timezone
from sqlmodel import SQLModel, Field, Relationship



class User(SQLModel, table=True):

    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True
    )

    username: str = Field(index=True, unique=True)
    email: str = Field(unique=True)

    hashed_password: str

    is_active: bool = True
    is_admin: bool = False


    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )


    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column_kwargs={
            "onupdate": lambda: datetime.now(timezone.utc),
        }
    )

    
