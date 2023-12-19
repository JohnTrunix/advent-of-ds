from sqlalchemy import BOOLEAN, TIMESTAMP, ForeignKey, Interval, String
from sqlalchemy.dialects.postgresql import ARRAY, UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql import func


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    uuid: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=func.uuid_generate_v4(),
    )
    github_id: Mapped[str] = mapped_column(
        String(255), unique=True, nullable=False
    )
    username: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    avatar_url: Mapped[str] = mapped_column(String(255))
    profile_url: Mapped[str] = mapped_column(String(255))
    oauth_token: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP, nullable=False, server_default=func.now()
    )


class Challenge(Base):
    __tablename__ = "challenges"

    uuid: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=func.uuid_generate_v4(),
    )
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    tags: Mapped[ARRAY] = mapped_column(ARRAY(String(64)), nullable=False)
    open_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, nullable=False)
    created_by: Mapped[str] = mapped_column(String(255), server_default=None)


class Submission(Base):
    __tablename__ = "submissions"

    uuid: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=func.uuid_generate_v4(),
    )
    user_uuid: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.uuid"), nullable=False
    )
    challenge_uuid: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("challenges.uuid"), nullable=False
    )
    opened_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, nullable=False)
    closed_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, server_default=None)
    duration: Mapped[Interval] = mapped_column(Interval, server_default=None)
    task_1: Mapped[BOOLEAN] = mapped_column(
        BOOLEAN, nullable=False, server_default="false"
    )
    task_2: Mapped[BOOLEAN] = mapped_column(
        BOOLEAN, nullable=False, server_default="false"
    )
