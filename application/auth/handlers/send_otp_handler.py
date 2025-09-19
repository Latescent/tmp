from application.auth.commands.send_otp_command import SendOtpCommand
from shared.unit_of_work import UnitOfWork
from domain.models.otp import Otp
from services.sms.sms_service import SmsService


class SendOtpHandler:
    def __init__(self, uow: UnitOfWork, sms_service: SmsService):
        self.uow = uow
        self.sms_service = sms_service

    async def handle(self, command: SendOtpCommand) -> None:
        otp = Otp.create(command.mobile)
        await self.sms_service.send_otp(mobile=otp.mobile, code=otp.code)
        async with self.uow as uow:
            await uow.otp_repo.create(otp)
            await uow.commit()
