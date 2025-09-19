from datetime import datetime
from sqlalchemy import String, Column, DateTime, Integer
from .base import Base


class Otp(Base):
    __tablename__ = 'otp'
    mobile: str = Column(String, nullable=False)
    code: int = Column(Integer, nullable=False)
    expire_at: datetime = Column(DateTime, nullable=False)
