from domain.models.loan_request import LoanRequest as DomainLoanRequest
from infrastructure.models.loan_request import LoanRequest as OrmLoanRequest
from infrastructure.mappers.auto_mapper import AutoMapper


class LoanRequestMapper(AutoMapper):
    domain_class = DomainLoanRequest
    orm_class = OrmLoanRequest