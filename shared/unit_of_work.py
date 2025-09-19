from typing import Callable
from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.db.session import async_session_factory
from infrastructure.repositories.access_token_repository import AccessTokenRepository
from infrastructure.repositories.file_relation_repository import FileRelationRepository
from infrastructure.repositories.file_repository import FileRepository
from infrastructure.repositories.otp_repository import OtpRepository
from infrastructure.repositories.user_repository import UserRepository
from infrastructure.repositories.enumeration_repository import EnumerationRepository
from infrastructure.repositories.guarantee_type_repository import GuaranteeTypeRepository
from infrastructure.repositories.loan_request_repository import LoanRequestRepository

REPOSITORIES = {
    'otp_repo': OtpRepository,
    'user_repo': UserRepository,
    'access_token_repo': AccessTokenRepository,
    'file_repo': FileRepository,
    'file_relation_repo': FileRelationRepository,
    'enumeration_repo': EnumerationRepository,
    'guarantee_type_repo': GuaranteeTypeRepository,
    'loan_request_repo': LoanRequestRepository,
}


class UnitOfWork:
    otp_repo: OtpRepository
    user_repo: UserRepository
    access_token_repo: AccessTokenRepository
    enumeration_repo: EnumerationRepository
    guarantee_type_repo: GuaranteeTypeRepository
    loan_request_repo: LoanRequestRepository

    def __init__(self, session_factory: Callable[[], AsyncSession]):
        self._session_factory = session_factory

    async def __aenter__(self):
        self._session = self._session_factory()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            await self.rollback()
        await self._session.close()

    async def commit(self):
        await self._session.commit()

    async def flush(self):
        await self._session.flush()


    async def rollback(self):
        await self._session.rollback()

    def __getattr__(self, name: str):
        try:
            repo_class = REPOSITORIES[name]
        except KeyError:
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")
        repo_instance = repo_class(self._session)
        setattr(self, name, repo_instance)
        return repo_instance


def get_unit_of_work() -> UnitOfWork:
    return UnitOfWork(session_factory=async_session_factory)
