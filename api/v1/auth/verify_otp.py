from fastapi import APIRouter, Depends, Body
from lib.translation_manager import tm
from application.auth.commands.verify_otp_command import VerifyOtpCommand
from application.auth.handlers.verify_otp_handler import VerifyOtpHandler
from application.dependencies.handlers import get_verify_otp_handler

router = APIRouter()


@router.post("/verify-otp")
async def verify_otp(handler: VerifyOtpHandler = Depends(get_verify_otp_handler),
                     command: VerifyOtpCommand = Body(...)):
    return {
        "message": tm(key='success'),
        "data": await handler.handle(command)
    }
