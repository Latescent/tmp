from fastapi import Depends
from application.auth.handlers.send_otp_handler import SendOtpHandler
from application.dependencies.get_current_user import get_current_user
from application.file.handlers.upload_file_handler import UploadFileHandler
from application.loan.handlers.create_loan_request_handler import CreateLoanRequestHandler
from config import config
from domain.models.user import User
from services.minio_service import MinioService
from application.auth.handlers.verify_otp_handler import VerifyOtpHandler
from services.sms.fake_sms_gateway import FakeSmsGateway
from services.sms.kavenegar_sms_gateway import KavenegarSmsGateway
from services.sms.sms_service import SmsService
from shared.unit_of_work import UnitOfWork, get_unit_of_work


def get_sms_sender() -> SmsService:
    if config.app_environment == "local":
        return SmsService(FakeSmsGateway())
    return SmsService(KavenegarSmsGateway())


def get_send_otp_handler(uow: UnitOfWork = Depends(get_unit_of_work),
                         sms_service: SmsService = Depends(get_sms_sender)
                         ) -> SendOtpHandler:
    return SendOtpHandler(uow=uow, sms_service=sms_service)


def get_minio_service() -> MinioService:
    secure = config.minio_secure
    return MinioService(secure=secure)


def get_upload_file_handler(
        uow: UnitOfWork = Depends(get_unit_of_work),
        current_user: User = Depends(get_current_user),
        minio_service: MinioService = Depends(get_minio_service)
) -> UploadFileHandler:
    return UploadFileHandler(uow=uow, current_user=current_user, minio_service=minio_service)


def get_verify_otp_handler(uow: UnitOfWork = Depends(get_unit_of_work)) -> VerifyOtpHandler:
    return VerifyOtpHandler(uow=uow)


def get_create_loan_request_handler(
        uow: UnitOfWork = Depends(get_unit_of_work),
        current_user: User = Depends(get_current_user)
) -> CreateLoanRequestHandler:
    return CreateLoanRequestHandler(uow=uow, current_user=current_user)
