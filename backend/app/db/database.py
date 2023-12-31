from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import get_settings

SQLALCHEMY_DATABASE_URL = get_settings().POSTGRES_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
