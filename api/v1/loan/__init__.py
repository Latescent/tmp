from fastapi import APIRouter
from .loan_request import router as loan_request_router

router = APIRouter()
router.include_router(loan_request_router)