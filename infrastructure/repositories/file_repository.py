from domain.models.file import File
from domain.repositories.file_repository import IFileRepository
from infrastructure.mappers.file_mapper import FileMapper
from infrastructure.repositories.base import BaseSqlAlchemyRepository


class FileRepository(BaseSqlAlchemyRepository, IFileRepository):
    async def create(self, file: File) -> File:
        orm_file = FileMapper.to_orm(file)
        self._session.add(orm_file)
        await self._session.flush()
        await self._session.refresh(orm_file)
        return FileMapper.to_domain(orm_file)
