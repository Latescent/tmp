from sqlalchemy import (
    Column, BigInteger, String, Integer, ForeignKey,
    TIMESTAMP, Double
)
from infrastructure.models.base import Base
from infrastructure.models.user import User


class File(Base):
    __tablename__ = "files"

    user_id = Column(BigInteger, ForeignKey(User.__tablename__ + ".id"), nullable=True)
    name = Column(String(255), nullable=False)
    path = Column(String(255), nullable=False)
    file_name = Column(String(255), nullable=False)
    mime_type = Column(String(255), nullable=False)
    format = Column(String(255), nullable=False)
    width = Column(Double, nullable=True)
    height = Column(Double, nullable=True)
    size = Column(Integer, nullable=False)
    type = Column(String(255), nullable=False)
    deleted_at = Column(TIMESTAMP(timezone=False), nullable=True)
