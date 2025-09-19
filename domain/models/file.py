from typing import Optional

from shared.exceptions import BusinessLogicException


class File:
    def __init__(
            self,
            id: Optional[int],
            user_id: int,
            name: str,
            path: str,
            file_name: str,
            mime_type: str,
            type: str,
            format: Optional[str] = None,
            width: Optional[int] = 0,
            height: Optional[int] = 0,
            size: int = 0
    ):
        if size < 0:
            raise BusinessLogicException("size must be >= 0")

        self.id = id
        self.user_id = user_id
        self.name = name
        self.path = path
        self.file_name = file_name
        self.mime_type = mime_type
        self.format = format
        self.width = width
        self.height = height
        self.size = size
        self.type = type

    @classmethod
    def create(
            cls,
            user_id: int,
            name: str,
            path: str,
            file_name: str,
            mime_type: str,
            type: str,
            format: Optional[str] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            size: int = 0,
    ) -> "File":
        return cls(
            id=None,
            user_id=user_id,
            name=name,
            path=path,
            file_name=file_name,
            mime_type=mime_type,
            format=format,
            width=width,
            height=height,
            size=size,
            type=type
        )

    def __str__(self) -> str:
        return f"{self.name} ({self.file_name})"
