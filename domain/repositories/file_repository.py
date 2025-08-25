from abc import ABC, abstractmethod

from domain.models.file import File


class IFileRepository(ABC):
    @abstractmethod
    async def create(self, file: File) -> None:
        ...
