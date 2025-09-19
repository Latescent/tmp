from fastapi import APIRouter, Depends, UploadFile, File, Form
from application.dependencies.handlers import get_upload_file_handler
from application.file.commands.upload_file_command import UploadFilesCommand, FileItem
from application.file.handlers.upload_file_handler import UploadFileHandler
from domain.enums.file_type_enum import FileTypeEnum
from lib.translation_manager import tm
from typing import List, Optional

from shared.exceptions import BusinessLogicException

router = APIRouter()


@router.post('/upload')
async def upload(
        files: List[UploadFile] = File(...),
        types: List[FileTypeEnum] = Form(...),
        entity_type: Optional[str] = Form(None),
        entity_id: Optional[int] = Form(None),
        handler: UploadFileHandler = Depends(get_upload_file_handler),
):
    if len(files) != len(types):
        raise BusinessLogicException(tm(key="files-types-count-mismatch"))
    command_files = [FileItem(file=f, type=t) for f, t in zip(files, types)]

    command = UploadFilesCommand(
        files=command_files,
        entity_type=entity_type,
        entity_id=entity_id,
    )

    return {
        "message": tm(key='success'),
        "data": await handler.handle(command)
    }
