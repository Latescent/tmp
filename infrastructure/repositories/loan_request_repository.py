from typing import Optional
from sqlalchemy import select
from domain.models.loan_request import LoanRequest
from infrastructure.mappers.loan_request_mapper import LoanRequestMapper
from infrastructure.models.loan_request import LoanRequest as OrmLoanRequest
from domain.repositories.loan_request_repository import ILoanRequestRepository
from infrastructure.repositories.base import BaseSqlAlchemyRepository


class LoanRequestRepository(BaseSqlAlchemyRepository, ILoanRequestRepository):
    async def get_by_loan_code(self, loan_code: str) -> Optional[LoanRequest]:
        stmt = (
            select(OrmLoanRequest)
            .where(OrmLoanRequest.loan_code == loan_code)
            .limit(1)
        )
        result = await self._session.execute(stmt)
        orm_loan_request = result.scalar_one_or_none()
        if orm_loan_request:
            return LoanRequestMapper.to_domain(orm_loan_request)
        return None

    async def create(self, loan_request: LoanRequest) -> LoanRequest:
        orm_loan_request = LoanRequestMapper.to_orm(loan_request)
        self._session.add(orm_loan_request)
        await self._session.flush()
        await self._session.refresh(orm_loan_request)
        return LoanRequestMapper.to_domain(orm_loan_request)