from abc import ABC, abstractmethod

from domain.models.file_relation import FileRelation


class IFileRelationRepository(ABC):
    @abstractmethod
    async def create(self, file_relation: FileRelation):
        ...
