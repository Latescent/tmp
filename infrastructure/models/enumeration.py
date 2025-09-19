from infrastructure.models.base import Base
from sqlalchemy import Column, BigInteger, String, ForeignKey


class Enumeration(Base):
    __tablename__ = "enumerations"

    title = Column(String(255), nullable=False)
    slug = Column(String(255), nullable=True)
    parent_id = Column(BigInteger, ForeignKey("enumerations.id"), nullable=True)