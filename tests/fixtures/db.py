import pytest

from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

from thunderbolt.core.settings import get_test_settings
from thunderbolt.models.base import ThunderboltModel


settings = get_test_settings()


@pytest.fixture(scope='function')
def mock_session():
    @asynccontextmanager
    async def session() -> AsyncSession:
        engine = create_async_engine(settings.DATABASE_URI, future=True)
        async with engine.begin() as conn:
            SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=conn, class_=AsyncSession)
            session: AsyncSession = SessionLocal()

            session.begin_nested()

            yield session

            await session.rollback()
        await engine.dispose()
    return session
