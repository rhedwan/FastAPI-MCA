import os
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

APP_ENV = os.getenv("APP_ENV", "development").lower()
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///blog.db")
TURSO_DATABASE_URL = os.getenv("TURSO_DATABASE_URL")
TURSO_AUTH_TOKEN = os.getenv("TURSO_AUTH_TOKEN")
SECRET_KEY = os.getenv("SECRET_KEY")


def pasrse_origins(value: str | None) -> list[str]:
    if not value:
        return []

    origins = [origin.strip().rstrip("/") for origin in value.split(",")]
    return [origin for origin in origins if origin]


#  https://blog.example.com, http://localhost:3000 -> ["https://blog.example.com","http://localhost:3000"]

CORS_ORIGINS = pasrse_origins(os.getenv("CORS_ORIGINS"))


using_turso = bool(TURSO_DATABASE_URL or TURSO_AUTH_TOKEN)

if  bool(TURSO_DATABASE_URL) != bool(TURSO_AUTH_TOKEN):
    raise RuntimeError(
        "TURSO_DATABASE_URL and TURSO_AUTH_TOKEN must be set together"
    )


if APP_ENV == "production" and not using_turso:
    raise RuntimeError(
            "TURSO_DATABASE_URL and TURSO_AUTH_TOKEN are required for production"
        )


if not SECRET_KEY:
    raise RuntimeError(
        "Missing required environment variables: SECRET_KEY"
    ) 


if "*" in CORS_ORIGINS:
    raise RuntimeError(
        "CORS_ORIGINS must list explict origins"
    ) 
