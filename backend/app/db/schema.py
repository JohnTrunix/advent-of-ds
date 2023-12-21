from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class Challenge(BaseModel):
    uuid: UUID
    day_id: int
    title: str
    tags: list[str]
    open_at: datetime
    created_by: str

    class Config:
        orm_mode = True


class Leaderboard(BaseModel):
    user_uuid: UUID
    username: str
    profile_url: str
    score: int
    mate: int
    total: int

    class Config:
        orm_mode = True
