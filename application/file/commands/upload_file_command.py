from typing import Optional, List
from pydantic import BaseModel, field_validator, Field
from domain.enums.file_type_enum import FileTypeEnum
from lib.translation_manager import tm
from fastapi import UploadFile

ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}


class FileItem(BaseModel):
    type: FileTypeEnum
    file: UploadFile

    @field_validator("file")
    @classmethod
    def validate_file_extension(cls, v: UploadFile):
        if v.filename:
            ext = v.filename.split('.')[-1].lower() if '.' in v.filename else ''
            if ext not in ALLOWED_EXTENSIONS:
                raise ValueError(tm(key="invalid-file-type"))
        return v


class UploadFilesCommand(BaseModel):
    files: List[FileItem] = Field(..., min_length=1)
    entity_type: Optional[int] = None
    entity_id: Optional[int] = None

    @field_validator("files")
    @classmethod
    def validate_files_not_empty(cls, v):
        if not v or len(v) == 0:
            raise ValueError(tm(key="files-required"))
        return v
