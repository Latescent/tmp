from infrastructure.models.base import Base
from infrastructure.models.user import User
from infrastructure.models.enumeration import Enumeration
from infrastructure.models.guarantee_type import GuaranteeType
from sqlalchemy import Column, BigInteger, String, SmallInteger, ForeignKey


class LoanRequest(Base):
    __tablename__ = "loan_requests"

    user_id = Column(BigInteger, ForeignKey(User.__tablename__ + ".id"), nullable=False)
    loan_code = Column(String(8), nullable=False, unique=True)
    amount = Column(BigInteger, nullable=False)
    status_id = Column(BigInteger, ForeignKey(Enumeration.__tablename__ + ".id"), nullable=False)
    guarantor_id = Column(BigInteger, ForeignKey(User.__tablename__ + ".id"), nullable=True)
    guarantee_type_id = Column(BigInteger, ForeignKey(GuaranteeType.__tablename__ + ".id"), nullable=False)
    installment_count = Column(SmallInteger, nullable=False)
    installment_amount = Column(BigInteger, nullable=False)