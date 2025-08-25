from .auth import router as auth_router
from .file import router as file_router
from fastapi import APIRouter

router = APIRouter()
router.include_router(auth_router, prefix='/auth', tags=["Authentication"])
router.include_router(file_router, prefix='/file', tags=["File"])
