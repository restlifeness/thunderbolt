import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from thunderbolt.core.settings import get_test_settings
from thunderbolt.models.base import ThunderboltModel


settings = get_test_settings()


@pytest.fixture(scope='function')
def mock_session():
    engine = create_engine(settings.DATABASE_URI)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()

    session.begin_nested()
    ThunderboltModel.metadata.create_all(bind=engine)

    yield session

    session.rollback()
    session.close()
