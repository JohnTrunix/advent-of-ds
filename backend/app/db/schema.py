from uuid import UUID

from pydantic import BaseModel


class Leaderboard(BaseModel):
    user_uuid: UUID
    username: str
    profile_url: str
    score: int
    mate: int
    total: int

    class Config:
        orm_mode = True
