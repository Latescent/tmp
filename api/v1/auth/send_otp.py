from fastapi import APIRouter, Body, Depends
from application.auth.commands.send_otp_command import SendOtpCommand
from application.auth.handlers.send_otp_handler import SendOtpHandler
from application.dependencies.handlers import get_send_otp_handler
from lib.translation_manager import tm

router = APIRouter()


@router.post("/send-otp")
async def send_otp(
        handler: SendOtpHandler = Depends(get_send_otp_handler),
        command: SendOtpCommand = Body(...)
):
    return {
        "message": tm(key='success'),
        "data": await handler.handle(command)
    }
