from abc import ABC, abstractmethod
from typing import Optional
from domain.models.guarantee_type import GuaranteeType


class IGuaranteeTypeRepository(ABC):
    @abstractmethod
    async def get_by_slug(self, slug: str) -> Optional[GuaranteeType]:
        pass

    @abstractmethod
    async def create(self, guarantee_type: GuaranteeType) -> GuaranteeType:
        pass