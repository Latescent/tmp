from os import path
from pydantic_settings import BaseSettings

curr_dir = path.dirname(__file__)


class Settings(BaseSettings):
    debug: bool = True
    app_title: str = "آوا پی"
    app_environment: str = "production"
    kavengar_api_key: str = ""
    kavengar_api_url: str = ""

    db_username: str = ""
    db_password: str = ""
    db_host: str = ""
    db_port: int = 5432
    db_name: str = ""

    minio_endpoint: str = ""
    minio_access_key: str = ""
    minio_secret_key: str = ""
    minio_bucket_name: str = ""
    minio_secure: bool = True

    minio_root_user: str = ""
    minio_root_password: str = ""

    class Config:
        case_sensitive: bool = False
        env_file: str = path.abspath(path.join(curr_dir, "../../.env"))
        env_file_encoding: str = "utf-8"

    @property
    def db_url(self) -> str:
        return f"postgresql+asyncpg://{self.db_username}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"


config = Settings()
