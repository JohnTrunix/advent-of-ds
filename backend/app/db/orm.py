from sqlalchemy import BOOLEAN, TIMESTAMP, ForeignKey, Integer, Interval, String
from sqlalchemy.dialects.postgresql import ARRAY, TEXT, UUID
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

    def __repr__(self):
        return (
            f"<User(uuid={self.uuid!r}, "
            f"github_id={self.github_id!r}, "
            f"username={self.username!r}, "
            f"email={self.email!r}, "
            f"avatar_url={self.avatar_url!r}, "
            f"profile_url={self.profile_url!r}, "
            f"oauth_token={self.oauth_token!r}, "
            f"created_at={self.created_at!r})>"
        )


class Challenge(Base):
    __tablename__ = "challenges"

    uuid: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=func.uuid_generate_v4(),
    )
    day_id: Mapped[int] = mapped_column(Integer, nullable=False, unique=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    tags: Mapped[ARRAY] = mapped_column(ARRAY(String(64)), nullable=False)
    open_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, nullable=False)
    created_by: Mapped[str] = mapped_column(String(255), server_default=None)
    content: Mapped[str] = mapped_column(
        TEXT, nullable=True, server_default=None
    )

    def __repr__(self):
        return (
            f"<Challenge(uuid={self.uuid!r}, "
            f"title={self.title!r}, "
            f"tags={self.tags!r}, "
            f"open_at={self.open_at!r}, "
            f"created_by={self.created_by!r})>"
            f"content={self.content!r})>"
        )


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

    def __repr__(self):
        return (
            f"<Submission(uuid={self.uuid!r}, "
            f"user_uuid={self.user_uuid!r}, "
            f"challenge_uuid={self.challenge_uuid!r}, "
            f"opened_at={self.opened_at!r}, "
            f"closed_at={self.closed_at!r}, "
            f"duration={self.duration!r}, "
            f"task_1={self.task_1!r}, "
            f"task_2={self.task_2!r})>"
        )
