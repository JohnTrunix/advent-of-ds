from functools import lru_cache

from app.config import Settings
from app.db.database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@lru_cache
def get_settings() -> Settings:
    return Settings()  # type: ignore
