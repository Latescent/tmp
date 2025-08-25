from abc import ABC, abstractmethod
from domain.models.otp import Otp
from domain.value_objects.mobile_number import MobileNumber


class IOtpRepository(ABC):
    @abstractmethod
    async def create(self, otp: Otp) -> Otp:
        ...

    @abstractmethod
    async def get_not_expired(self, mobile: MobileNumber, code: int) -> Otp | None:
        ...
