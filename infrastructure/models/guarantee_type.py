from infrastructure.models.base import Base
from sqlalchemy import Column, String, Integer


class GuaranteeType(Base):
    __tablename__ = "guarantee_types"

    title = Column(String(255), nullable=False)
    slug = Column(String(255), nullable=True)
    max_loan_amount = Column(Integer, nullable=True)