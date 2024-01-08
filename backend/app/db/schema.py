from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class Challenges(BaseModel):
    uuid: UUID
    day_id: int
    title: str
    tags: list[str]
    open_at: datetime
    created_by: str

    class ConfigDict:
        from_attributes = True


class Challenge(Challenges):
    content: str | None

    class ConfigDict:
        from_attributes = True


class Leaderboard(BaseModel):
    user_uuid: UUID
    username: str
    profile_url: str
    avatar_url: str
    score: int
    mate: int
    total: int

    class ConfigDict:
        from_attributes = True


class User(BaseModel):
    username: str
    email: str
    avatar_url: str
    profile_url: str
    oauth_token: str

    class ConfigDict:
        from_attributes = True


class UserCreate(User):
    github_id: str


class UserRead(User):
    uuid: UUID
    github_id: str
