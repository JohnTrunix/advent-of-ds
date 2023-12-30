import os
from functools import lru_cache

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    OAUTH_CLIENT_ID: str = os.getenv("OAUTH_CLIENT_ID") or "client_id"
    OAUTH_CLIENT_SECRET: str = (
        os.getenv("OAUTH_CLIENT_SECRET") or "client_secret"
    )
    OAUTH_SCOPE: str = os.getenv("OAUTH_SCOPE") or "scope"
    OAUTH_AUTHORIZE_URL: str = (
        os.getenv("OAUTH_AUTHORIZE_URL") or "authorize_url"
    )
    OAUTH_TOKEN_URL: str = os.getenv("OAUTH_TOKEN_URL") or "token_url"
    OAUTH_REDIRECT_URL: str = os.getenv("OAUTH_REDIRECT_URL") or "redirect_url"
    POSTGRES_URL: str = os.getenv("POSTGRES_URL") or "postgres_url"


@lru_cache
def get_settings() -> Settings:
    return Settings()  # type: ignore
