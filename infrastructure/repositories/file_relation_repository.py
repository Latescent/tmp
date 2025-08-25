from domain.models.file_relation import FileRelation
from domain.repositories.file_relation_repository import IFileRelationRepository
from infrastructure.mappers.file_relation_mapper import FileRelationMapper
from infrastructure.repositories.base import BaseSqlAlchemyRepository


class FileRelationRepository(BaseSqlAlchemyRepository, IFileRelationRepository):
    async def create(self, file_relation: FileRelation):
        orm_file_relation = FileRelationMapper.to_orm(file_relation)
        self._session.add(orm_file_relation)
        await self._session.flush()
        await self._session.refresh(orm_file_relation)
        return FileRelationMapper.to_domain(orm_file_relation)
