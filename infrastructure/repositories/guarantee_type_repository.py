from typing import Optional
from sqlalchemy import select
from domain.models.guarantee_type import GuaranteeType
from infrastructure.mappers.guarantee_type_mapper import GuaranteeTypeMapper
from infrastructure.models.guarantee_type import GuaranteeType as OrmGuaranteeType
from domain.repositories.guarantee_type_repository import IGuaranteeTypeRepository
from infrastructure.repositories.base import BaseSqlAlchemyRepository


class GuaranteeTypeRepository(BaseSqlAlchemyRepository, IGuaranteeTypeRepository):
    async def get_by_slug(self, slug: str) -> Optional[GuaranteeType]:
        stmt = (
            select(OrmGuaranteeType)
            .where(OrmGuaranteeType.slug == slug)
            .limit(1)
        )
        result = await self._session.execute(stmt)
        orm_guarantee_type = result.scalar_one_or_none()
        if orm_guarantee_type:
            return GuaranteeTypeMapper.to_domain(orm_guarantee_type)
        return None

    async def create(self, guarantee_type: GuaranteeType) -> GuaranteeType:
        orm_guarantee_type = GuaranteeTypeMapper.to_orm(guarantee_type)
        self._session.add(orm_guarantee_type)
        await self._session.flush()
        await self._session.refresh(orm_guarantee_type)
        return GuaranteeTypeMapper.to_domain(orm_guarantee_type)