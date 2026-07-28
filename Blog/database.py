from sqlmodel import Session, create_engine

from config import DATABASE_URL, TURSO_AUTH_TOKEN, TURSO_DATABASE_URL, using_turso

#  manages communication with the database
#  FastAPI -> Engine -> Database


print(f"sqlite+{TURSO_DATABASE_URL}?secure=true")
if using_turso:
    engine = create_engine(
        f"sqlite+{TURSO_DATABASE_URL}?secure=true",
        connect_args={"auth_token": TURSO_AUTH_TOKEN},
        pool_pre_ping=True
    )
else:
    engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)


def get_db():
    with Session(engine) as session:
        yield session
    
