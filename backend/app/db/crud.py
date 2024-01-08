from sqlalchemy import text
from sqlalchemy.orm import Session

from app.db import orm, schema


def get_challenges(db: Session) -> list[schema.Challenges]:
    result = (
        db.query(
            orm.Challenge.uuid,
            orm.Challenge.day_id,
            orm.Challenge.title,
            orm.Challenge.tags,
            orm.Challenge.open_at,
            orm.Challenge.created_by,
        )
        .order_by(orm.Challenge.day_id)
        .all()
    )
    return result  # type: ignore


def get_challenge_by_uuid(db: Session, uuid: str) -> schema.Challenge:
    result = db.query(orm.Challenge).filter(orm.Challenge.uuid == uuid).first()
    return result  # type: ignore


def get_leaderboard(db: Session) -> list[schema.Leaderboard]:
    result = db.execute(text("SELECT * FROM leaderboard;")).fetchall()
    return result  # type: ignore
