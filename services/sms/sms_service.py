from domain.value_objects.mobile_number import MobileNumber
from lib.translation_manager import tm
from services.sms.base_sms_gateway import ISmsGateway
from dataclasses import dataclass


@dataclass
class SmsResult:
    success: bool
    message: str


class SmsService:
    def __init__(self, sms_gateway: ISmsGateway):
        self.gateway = sms_gateway

    def build_otp_message(cls, code: int) -> str:
        return tm(key='otp-code', code=code)

    async def send_otp(self, mobile: MobileNumber, code: int) -> SmsResult:
        message = self.build_otp_message(code)
        success = await self.gateway.send(mobile.value, message)
        return SmsResult(success=success, message=message)

    async def send_custom(self, mobile: str, key: str, **kwargs) -> SmsResult:
        message = tm(key=key, **kwargs)
        success = await self.gateway.send(mobile, message)
        return SmsResult(success=success, message=message)
