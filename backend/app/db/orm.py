from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.dialects.postgresql import UUID


class Users:
    __tablename__ = "users"

    uuid: Mapped[UUID] = mapped_column(primary_key=True, default=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    score: Mapped[int] = mapped_column(default=0)
    coffees: Mapped[int] = mapped_column(default=0)
