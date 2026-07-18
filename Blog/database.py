from  sqlalchemy.orm import DeclarativeBase
from sqlmodel import Session, create_engine


DATABASE_URL = "sqlite:///blog.db"


#  manages communication with the database
#  FastAPI -> Engine -> Database
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)


class Base(DeclarativeBase):
    pass


def get_db():
    with Session(engine) as session:
        yield session
    