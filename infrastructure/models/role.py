from sqlalchemy import Column, BigInteger, String
from .base import Base


class Role(Base):
    __tablename__ = "roles"

    id = Column(BigInteger, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    title = Column(String(255), nullable=False, unique=True)
