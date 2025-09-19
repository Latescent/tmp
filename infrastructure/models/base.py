from sqlalchemy import Column, DateTime
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from shared.helpers import now_iran


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), default=now_iran, nullable=True)
    updated_at = Column(DateTime(timezone=True), default=now_iran, onupdate=now_iran, nullable=True)
