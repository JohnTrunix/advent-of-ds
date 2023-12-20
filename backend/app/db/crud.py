from sqlalchemy import text
from sqlalchemy.orm import Session

from app.db import schema


def get_leaderboard(db: Session) -> list[schema.Leaderboard]:
    result = db.execute(text("SELECT * FROM leaderboard;")).fetchall()
    return result  # type: ignore
