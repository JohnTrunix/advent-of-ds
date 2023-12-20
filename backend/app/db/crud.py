from sqlalchemy import text
from sqlalchemy.orm import Session

from app.db import orm, schema


def get_challenges(db: Session) -> list[schema.Challenge]:
    result = db.query(orm.Challenge).order_by(orm.Challenge.day_id).all()
    return result  # type: ignore


def get_challenge_by_day_id(db: Session, day_id: str) -> schema.Challenge:
    result = (
        db.query(orm.Challenge).filter(orm.Challenge.day_id == day_id).first()
    )
    return result  # type: ignore


def get_leaderboard(db: Session) -> list[schema.Leaderboard]:
    result = db.execute(text("SELECT * FROM leaderboard;")).fetchall()
    return result  # type: ignore
