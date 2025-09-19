from sqlalchemy import Column, BigInteger, ForeignKey, String

from infrastructure.models.base import Base
from infrastructure.models.file import File


class FileRelation(Base):
    __tablename__ = 'file_relations'
    entity_id = Column(BigInteger, nullable=False)
    entity_type = Column(String, nullable=False)
    file_id = Column(BigInteger, ForeignKey(File.__tablename__ + ".id"), nullable=False)
