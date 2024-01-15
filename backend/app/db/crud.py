from sqlalchemy import text
from sqlalchemy.dialects.postgresql import insert
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


def create_user(db: Session, user: schema.UserCreate) -> schema.User:
    db_user = orm.User(
        github_id=user.github_id,
        username=user.username,
        email=user.email,
        avatar_url=user.avatar_url,
        profile_url=user.profile_url,
        oauth_token=user.oauth_token,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user  # type: ignore


def create_update_user(db: Session, user: schema.UserCreate) -> schema.User:
    stmt = (
        insert(orm.User)
        .values(
            github_id=user.github_id,
            username=user.username,
            email=user.email,
            avatar_url=user.avatar_url,
            profile_url=user.profile_url,
            oauth_token=user.oauth_token,
        )
        .on_conflict_do_update(
            index_elements=[orm.User.github_id],
            set_=dict(
                username=user.username,
                email=user.email,
                avatar_url=user.avatar_url,
                profile_url=user.profile_url,
                oauth_token=user.oauth_token,
            ),
        )
    )
    result = db.execute(stmt)
    db.commit()
    return result  # type: ignore
