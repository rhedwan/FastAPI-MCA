from datetime import datetime, timezone
from sqlalchemy import Integer, String, Boolean, DateTime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from Relationships.database import Base


class Todo(Base):

    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(
        Integer, 
        primary_key= True,
        index=True
    )

    title:  Mapped[str] = mapped_column(String, index=True)
    description: Mapped[str | None] = mapped_column(String)
    completed: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda:datetime.now(timezone.utc))




