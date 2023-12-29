from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    OAUTH_CLIENT_ID: str
    OAUTH_CLIENT_SECRET: str
    OAUTH_SCOPE: str
    OAUTH_AUTHORIZE_URL: str
    OAUTH_TOKEN_URL: str
    OAUTH_REDIRECT_URL: str
    POSTGRES_URL: str

    model_config = SettingsConfigDict(env_file="app/.env")
