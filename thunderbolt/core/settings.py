import os

from dotenv import load_dotenv
from pydantic import BaseSettings


TEST_DB_URI = "sqlite+aiosqlite:///./test.db"


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

    JWT_SECRET: str = 'thunderbolt@secret'
    JWT_ALGORITHM: str = 'HS256'

    HASH_METHOD: str = 'scrypt'
    SALT_LENGTH: int = 16

    SERVER_TIMEZONE: str = 'UTC'

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


def get_async_db_uri_from_env():
    load_dotenv()
    postgres_user = os.environ.get('POSTGRES_USER')
    postgres_password = os.environ.get('POSTGRES_PASSWORD')
    postgres_db = os.environ.get('POSTGRES_DB')
    postgres_port = os.environ.get('POSTGRES_PORT')
    postgres_host = os.environ.get('POSTGRES_HOST')
    return f"postgresql+asyncpg://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}"

# TODO: Remove this function

def get_sync_db_uri_from_env():
    load_dotenv()
    postgres_user = os.environ.get('POSTGRES_USER')
    postgres_password = os.environ.get('POSTGRES_PASSWORD')
    postgres_db = os.environ.get('POSTGRES_DB')
    postgres_port = os.environ.get('POSTGRES_PORT')
    postgres_host = os.environ.get('POSTGRES_HOST')
    return f"postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}"


def get_settings():
    DATABASE_URI = get_async_db_uri_from_env()
    return ApplicationSettings(DATABASE_URI=DATABASE_URI)


def get_test_settings():
    DATABASE_URI = get_async_db_uri_from_env()
    return ApplicationSettings(DATABASE_URI=DATABASE_URI)
