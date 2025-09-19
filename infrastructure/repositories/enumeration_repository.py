from typing import Optional
from sqlalchemy import select
from domain.models.enumeration import Enumeration
from infrastructure.mappers.enumeration_mapper import EnumerationMapper
from infrastructure.models.enumeration import Enumeration as OrmEnumeration
from domain.repositories.enumeration_repository import IEnumerationRepository
from infrastructure.repositories.base import BaseSqlAlchemyRepository


class EnumerationRepository(BaseSqlAlchemyRepository, IEnumerationRepository):
    async def get_by_slug(self, slug: str) -> Optional[Enumeration]:
        stmt = (
            select(OrmEnumeration)
            .where(OrmEnumeration.slug == slug)
            .limit(1)
        )
        result = await self._session.execute(stmt)
        orm_enumeration = result.scalar_one_or_none()
        if orm_enumeration:
            return EnumerationMapper.to_domain(orm_enumeration)
        return None

    async def get_by_parent_id_and_slug(self, parent_id: int, slug: str) -> Optional[Enumeration]:
        stmt = (
            select(OrmEnumeration)
            .where(
                OrmEnumeration.parent_id == parent_id,
                OrmEnumeration.slug == slug
            )
            .limit(1)
        )
        result = await self._session.execute(stmt)
        orm_enumeration = result.scalar_one_or_none()
        if orm_enumeration:
            return EnumerationMapper.to_domain(orm_enumeration)
        return None

    async def create(self, enumeration: Enumeration) -> Enumeration:
        orm_enumeration = EnumerationMapper.to_orm(enumeration)
        self._session.add(orm_enumeration)
        await self._session.flush()
        await self._session.refresh(orm_enumeration)
        return EnumerationMapper.to_domain(orm_enumeration)