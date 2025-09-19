from abc import ABC, abstractmethod
from typing import Optional
from domain.models.enumeration import Enumeration


class IEnumerationRepository(ABC):
    @abstractmethod
    async def get_by_slug(self, slug: str) -> Optional[Enumeration]:
        pass

    @abstractmethod
    async def get_by_parent_id_and_slug(self, parent_id: int, slug: str) -> Optional[Enumeration]:
        pass

    @abstractmethod
    async def create(self, enumeration: Enumeration) -> Enumeration:
        pass