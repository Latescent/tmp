from typing import Optional
from datetime import datetime
from shared.helpers import now_iran


class LoanRequest:
    def __init__(self, user_id: int, loan_code: str, amount: int, status_id: int,
                 guarantee_type_id: int, installment_count: int, installment_amount: int, **kwargs) -> None:
        self.id: Optional[int] = kwargs.get('id')
        self.user_id: int = user_id
        self.loan_code: str = loan_code
        self.amount: int = amount
        self.status_id: int = status_id
        self.guarantor_id: Optional[int] = kwargs.get('guarantor_id')
        self.guarantee_type_id: int = guarantee_type_id
        self.installment_count: int = installment_count
        self.installment_amount: int = installment_amount
        self.created_at: datetime = kwargs.get('created_at', now_iran())
        self.updated_at: datetime = kwargs.get('updated_at', now_iran())

    @classmethod
    def create(cls, user_id: int, loan_code: str, amount: int, status_id: int,
               guarantee_type_id: int, installment_count: int, installment_amount: int,
               guarantor_id: Optional[int] = None):
        return cls(
            user_id=user_id,
            loan_code=loan_code,
            amount=amount,
            status_id=status_id,
            guarantee_type_id=guarantee_type_id,
            installment_count=installment_count,
            installment_amount=installment_amount,
            guarantor_id=guarantor_id
        )