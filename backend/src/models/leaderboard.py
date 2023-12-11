from datetime import datetime

from pydantic import BaseModel, Field


class LeaderboardEntry(BaseModel):
    id: int
    name: str
    score: int
    coffees: int


class Leaderboard(BaseModel):
    entries: list[LeaderboardEntry]
    request_time: datetime = Field(default_factory=datetime.now)
