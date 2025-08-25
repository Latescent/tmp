from dataclasses import dataclass
from application.auth.commands.verify_otp_command import VerifyOtpCommand
from domain.models.access_token import AccessToken
from domain.value_objects.mobile_number import MobileNumber
from shared.exceptions import UnauthorizedError
from shared.unit_of_work import UnitOfWork
from domain.models.otp import Otp
from domain.models.user import User


@dataclass
class Result:
    token: str


class VerifyOtpHandler:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def handle(self, command: VerifyOtpCommand) -> Result:
        async with self.uow as uow:
            not_expired_otp: Otp | None = await uow.otp_repo.get_not_expired(
                mobile=MobileNumber(command.mobile),
                code=command.code,
            )

            if not not_expired_otp:
                raise UnauthorizedError()

            user = await uow.user_repo.get_by_mobile(not_expired_otp.mobile)
            if user is None:
                user = User.create(
                    mobile=str(not_expired_otp.mobile),
                    role_id=2
                )
                user = await uow.user_repo.create(user)
                await uow.commit()
            token = AccessToken.create(user.id)
            await uow.access_token_repo.create(token)
            await uow.commit()
            return Result(token=str(token))
