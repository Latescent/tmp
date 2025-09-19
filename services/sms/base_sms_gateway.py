from abc import ABC, abstractmethod


class ISmsGateway(ABC):

    @abstractmethod
    async def send(self, recipient: str, body: str, **extra) -> bool:
        ...
