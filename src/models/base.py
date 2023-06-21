import uuid

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

from src.core.settings import get_settings


Base = declarative_base()
settings = get_settings()


class ThunderboltModel(Base):
    __abstract__ = True

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)

    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())
