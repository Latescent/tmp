from sqlalchemy.ext.asyncio import AsyncSession


class BaseSqlAlchemyRepository:
    def __init__(self, session: AsyncSession):
        self._session = session
