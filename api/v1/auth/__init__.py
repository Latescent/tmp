from fastapi import APIRouter
from .send_otp import router as send_otp_router
from .verify_otp import router as verify_otp_router

router = APIRouter()
router.include_router(send_otp_router)
router.include_router(verify_otp_router)
