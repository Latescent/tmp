from os import path
from pydantic_settings import BaseSettings
from pydantic import ConfigDict

curr_dir = path.dirname(__file__)


class Settings(BaseSettings):
    debug: bool = True
    app_title: str = "آوا پی"
    app_environment: str = "production"

    kavenegar_api_key: str = ""
    kavenegar_api_url: str = ""
    kavenegar_sender: str = ""

    shahkar_business_id: str = ""
    shahkar_business_token: str = ""
    shahkar_api_url: str = "https://json-api.uid.ir/api/inquiry/mobile/owner/v2"

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

    model_config = ConfigDict(
        case_sensitive=False,
        env_file=path.abspath(path.join(curr_dir, "../../.env")),
        env_file_encoding="utf-8"
    )

    @property
    def db_url(self) -> str:
        return f"postgresql+asyncpg://{self.db_username}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"


config = Settings()
