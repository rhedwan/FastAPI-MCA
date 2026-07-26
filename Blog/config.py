import os
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")

missing_variables = [
    name
    for name, value in {
        "DATABASE_URL": DATABASE_URL,
        "SECRET_KEY": SECRET_KEY,
    }.items()
    if not value
]

if missing_variables:
    missing = ", ".join(missing_variables)
    raise RuntimeError(f"Missing required environment variables: {missing}")
