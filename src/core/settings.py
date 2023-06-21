
from pydantic import BaseSettings


TEST_DB_URI = "sqlite:///./test.db"


class ApplicationSettings(BaseSettings):
    APP_NAME: str = "Thunderbolt"

    DATABASE_URI: str = None

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_PORT: int
    POSTGRES_HOST: str

    REDIS_PORT: int
    REDIS_HOST: str

    HASH_METHOD: str = 'sha256'
    SALT_LENGTH: int = 16

    SERVER_TIMEZONE: str = 'UTC'

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


def get_settings():
    return ApplicationSettings()


def get_test_settings():
    return ApplicationSettings(DATABASE_URI=TEST_DB_URI)
