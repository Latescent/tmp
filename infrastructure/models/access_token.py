from datetime import datetime
from sqlalchemy import String, Column, DateTime, Integer, ForeignKey, TIMESTAMP
from sqlalchemy.orm import mapped_column, Mapped

from .base import Base
from .user import User


class AccessToken(Base):
    __tablename__ = 'access_tokens'

    token: str = Column(String(255), unique=True, nullable=False, index=True)
    user_id: int = Column(Integer, ForeignKey(f"{User.__tablename__}.id", ondelete='CASCADE'), nullable=False)
    expires_at: Mapped[DateTime] = mapped_column(TIMESTAMP(timezone=True), nullable=True)
