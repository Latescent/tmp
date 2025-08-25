from typing import Optional, List, Set
from sqlalchemy import select, update
from sqlalchemy import select, and_, or_
from domain.models.user import User
from infrastructure.mappers.user_mapper import UserMapper
from infrastructure.models.user import User as OrmUser
from domain.repositories.user_repository import IUserRepository
from domain.value_objects.mobile_number import MobileNumber
from infrastructure.repositories.base import BaseSqlAlchemyRepository
from infrastructure.models.access_token import AccessToken as OrmAccessToken
from sqlalchemy import func


class UserRepository(BaseSqlAlchemyRepository, IUserRepository):
    async def get_by_token(self, token_hash: str) -> Optional[User]:
        stmt = (
            select(OrmUser)
            .join(OrmAccessToken, OrmUser.id == OrmAccessToken.tokenable_id)
            .where(
                and_(
                    OrmAccessToken.token == token_hash,
                    OrmAccessToken.tokenable_type == "4",
                    or_(
                        OrmAccessToken.expires_at.is_(None),
                        OrmAccessToken.expires_at > func.now()
                    )
                )
            )
            .limit(1)
        )
        result = await self._session.execute(stmt)
        orm_user = result.scalar_one_or_none()

        if orm_user:
            return UserMapper.to_domain(orm_user)
        return None

    async def get_by_mobile(self, mobile: MobileNumber) -> Optional[User]:
        stmt = (
            select(OrmUser)
            .where(
                OrmUser.mobile == str(mobile),
                OrmUser.mobile == str(mobile)
            )
            .limit(1)
        )
        result = await self._session.execute(stmt)
        orm_user = result.scalar_one_or_none()
        if orm_user:
            return UserMapper.to_domain(orm_user)
        return None

    async def update(self, user: User, fields: Optional[Set[str]] = None) -> None:
        if not fields:
            fields = {key for key in vars(user) if key != "id"}

        values = {
            field: getattr(user, field)
            for field in fields
            if hasattr(user, field)
        }

        stmt = (
            update(OrmUser)
            .where(OrmUser.id == user.id)
            .values(**values)
        )

        await self._session.execute(stmt)
        await self._session.flush()

        refreshed = await self._session.get(OrmUser, user.id)
        if refreshed is None:
            raise ValueError(f"User with id {user.id} not found after update")

        return UserMapper.to_domain(refreshed)

    async def get_by_id(self, user_id: int) -> Optional[User]:
        stmt = (
            select(OrmUser)
            .where(
                OrmUser.id == user_id
            )
            .limit(1)
        )
        result = await self._session.execute(stmt)
        orm_user = result.scalar_one_or_none()
        if orm_user:
            return UserMapper.to_domain(orm_user)
        return None

    async def create(self, user: User) -> User:
        orm_user = UserMapper.to_orm(user)
        self._session.add(orm_user)
        await self._session.flush()
        await self._session.refresh(orm_user)
        return UserMapper.to_domain(orm_user)
