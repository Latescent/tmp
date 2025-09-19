from pydantic import BaseModel
from typing import Optional


class CreateLoanRequestCommand(BaseModel):
    amount: int
    guarantee_type: str
    installment_count: int
    installment_amount: int
    guarantor_id: Optional[int] = None