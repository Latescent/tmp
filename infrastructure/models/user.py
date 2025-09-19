from infrastructure.models.base import Base
from infrastructure.models.role import Role
from sqlalchemy import Column, BigInteger, String, ForeignKey


class User(Base):
    __tablename__ = "users"

    role_id = Column(BigInteger, ForeignKey(Role.__tablename__ + ".id"), nullable=False)
    first_name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=True)
    mobile = Column(String(15), nullable=False)
    national_code = Column(String(15), nullable=True)
