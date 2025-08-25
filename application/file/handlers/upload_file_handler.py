from application.file.commands.upload_file_command import UploadFilesCommand
from domain.models.file import File
from domain.models.file_relation import FileRelation
from domain.models.user import User
from shared.unit_of_work import UnitOfWork
from datetime import datetime
import random, string, os
from services.minio_service import MinioService


class UploadFileHandler:
    def __init__(self, uow: UnitOfWork, current_user: User, minio_service: MinioService):
        self.uow = uow
        self.current_user = current_user
        self.minio_service = minio_service

    async def handle(self, command: UploadFilesCommand):
        async with self.uow as uow:
            saved_files = []
            for file_item in command.files:
                original_name = file_item.file.filename
                ext = os.path.splitext(original_name)[1]
                random_name = self._random_string(50)

                path = f"clinic/12/{file_item.type.value}/{datetime.now().strftime('%y%m')}"
                object_name = f"{path}/{random_name}{ext}"

                contents = await file_item.file.read()
                await file_item.file.seek(0)

                await self.minio_service.upload_file(
                    object_name=object_name,
                    data=contents,
                    content_type=file_item.file.content_type
                )

                domain_file: File = File.create(
                    user_id=self.current_user.id,
                    name=random_name + ext,
                    path=path,
                    file_name=random_name,
                    mime_type=file_item.file.content_type,
                    format=ext.lstrip("."),
                    size=len(contents),
                    type=file_item.type.value,
                )
                domain_file = await uow.file_repo.create(domain_file)
                await uow.commit()

                domain_file_relation = FileRelation.create(self.current_user.id, 4, domain_file.id)
                await uow.file_relation_repo.create(domain_file_relation)
                saved_files.append(domain_file)

            await uow.commit()
            return saved_files

    async def _get_file_size(self, file_item):
        contents = await file_item.read()
        size = len(contents)
        await file_item.seek(0)
        return size

    def _random_string(self, length=50):
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(length))
