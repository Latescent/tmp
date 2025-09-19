from abc import ABC, abstractmethod

from domain.models.access_token import AccessToken


class IAccessTokenRepository(ABC):
    @abstractmethod
    async def create(self, access_token: AccessToken) -> AccessToken:
        ...
