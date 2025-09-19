from abc import ABC, abstractmethod
from typing import Optional
from domain.models.loan_request import LoanRequest


class ILoanRequestRepository(ABC):
    @abstractmethod
    async def get_by_loan_code(self, loan_code: str) -> Optional[LoanRequest]:
        pass

    @abstractmethod
    async def create(self, loan_request: LoanRequest) -> LoanRequest:
        pass