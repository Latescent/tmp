from fastapi import APIRouter, Body, Depends
from application.loan.commands.create_loan_request_command import CreateLoanRequestCommand
from application.loan.handlers.create_loan_request_handler import CreateLoanRequestHandler
from application.dependencies.handlers import get_create_loan_request_handler
from lib.translation_manager import tm

router = APIRouter()


@router.post("/loan-request")
async def create_loan_request(
        handler: CreateLoanRequestHandler = Depends(get_create_loan_request_handler),
        command: CreateLoanRequestCommand = Body(...)
):
    await handler.handle(command)
    return {
        "message": tm(key='success')
    }