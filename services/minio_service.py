import asyncio
import io
from concurrent.futures import ThreadPoolExecutor
from os import SEEK_END, SEEK_SET
from typing import Optional, Union
from minio import Minio
from minio.error import S3Error
from config import config


class MinioService:
    def __init__(self, secure: bool = True):
        self.client = Minio(
            config.minio_endpoint,
            access_key=config.minio_access_key,
            secret_key=config.minio_secret_key,
            secure=secure
        )
        self.executor = ThreadPoolExecutor(max_workers=5)

    async def upload_file(
            self,
            object_name: str,
            data: Union[bytes, io.BytesIO],
            content_type: str,
            bucket_name: Optional[str] = None
    ):
        bucket = bucket_name or config.minio_bucket_name

        await self._ensure_bucket_exists(bucket)

        loop = asyncio.get_event_loop()

        try:
            if isinstance(data, bytes):
                data_stream = io.BytesIO(data)
                length = len(data)
            else:
                data_stream = data
                data_stream.seek(0, SEEK_END)
                length = data_stream.tell()
                data_stream.seek(0)
                data_stream.seek(0, SEEK_SET)

            await loop.run_in_executor(
                self.executor,
                lambda: self.client.put_object(
                    bucket_name=bucket,
                    object_name=object_name,
                    data=data_stream,
                    length=length,
                    content_type=content_type
                )
            )

        except S3Error as e:
            raise Exception(f"Failed to upload {object_name}: {str(e)}")

    async def download_file(self, object_name: str, bucket_name: Optional[str] = None) -> bytes:
        bucket = bucket_name or config.bucket_name
        loop = asyncio.get_event_loop()

        try:
            response = await loop.run_in_executor(
                self.executor,
                lambda: self.client.get_object(bucket, object_name)
            )
            data = response.read()
            response.close()
            response.release_conn()
            return data

        except S3Error as e:
            raise Exception(f"Failed to download {object_name}: {str(e)}")

    async def file_exists(self, object_name: str, bucket_name: Optional[str] = None) -> bool:
        bucket = bucket_name or config.bucket_name
        loop = asyncio.get_event_loop()

        try:
            await loop.run_in_executor(
                self.executor,
                lambda: self.client.stat_object(bucket, object_name)
            )
            return True
        except S3Error:
            return False

    async def _ensure_bucket_exists(self, bucket_name: str):
        loop = asyncio.get_event_loop()

        bucket_exists = await loop.run_in_executor(
            self.executor,
            lambda: self.client.bucket_exists(bucket_name)
        )

        if not bucket_exists:
            await loop.run_in_executor(
                self.executor,
                lambda: self.client.make_bucket(bucket_name)
            )

    def close(self):
        self.executor.shutdown(wait=True)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.close()
