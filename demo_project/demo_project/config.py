from pydantic import SecretStr, ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    OBJECT_STORAGE_URL: str
    MINIO_ACCESS_KEY_ID: SecretStr
    MINIO_SECRET_ACCESS_KEY: SecretStr
    MLFLOW_ADMIN_USER: str = "admin"
    MLFLOW_ADMIN_PASSWORD: SecretStr

    model_config = ConfigDict(env_file=".env", env_file_encoding="utf-8", extra="allow")


settings = Settings()
