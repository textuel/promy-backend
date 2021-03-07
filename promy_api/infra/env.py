from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Promy API"
    version: str
    environment: str
    app_url: str
    aws_access_key_id: str
    aws_secret_access_key: str
    db_url: str
    db_user: str
    db_password: str
    s3_bucket: str
    s3_region: str

    class Config:
        env_file = ".env"


settings = Settings()
