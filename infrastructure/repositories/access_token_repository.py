from domain.models.access_token import AccessToken
from domain.repositories.access_token_repository import IAccessTokenRepository
from infrastructure.mappers.access_token_mapper import AccessTokenMapper
from infrastructure.repositories.base import BaseSqlAlchemyRepository


class AccessTokenRepository(IAccessTokenRepository, BaseSqlAlchemyRepository):
    async def create(self, access_token: AccessToken) -> AccessToken:
        orm_token = AccessTokenMapper.to_orm(access_token)
        self._session.add(orm_token)
        await self._session.flush()
        await self._session.refresh(orm_token)
        return AccessTokenMapper.to_domain(orm_token)
