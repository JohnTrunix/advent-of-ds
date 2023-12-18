from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column


class Users:
    __tablename__ = "users"

    uuid: Mapped[UUID] = mapped_column(primary_key=True, default=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    score: Mapped[int] = mapped_column(default=0)
    coffees: Mapped[int] = mapped_column(default=0)
