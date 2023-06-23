
from typing import Annotated
from fastapi import Depends

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from thunderbolt.core.session import get_session
from thunderbolt.core.base import AbstractRepository
from thunderbolt.models import Topic


class TopicRepository(AbstractRepository):
    """
    Repository class for Topic model

    This class encapsulates the database access for the Topic model. It provides
    functions for adding, getting, and deleting topic records.
    """

    def __init__(self, session: Annotated[AsyncSession, Depends(get_session)]):
        """
        Initialize the TopicRepository class.

        Args:
            session (AsyncSession): SQLAlchemy Session for database access
        """
        self._session = session

    async def add(self, topic: Topic) -> None:
        """
        Add a new Topic to the database.

        Args:
            topic (Topic): Topic object to be added
        """
        self._session.add(topic)
        await self._session.flush()

    async def update(self, topic: Topic) -> None:
        """
        Update a Topic in the database.

        Args:
            topic (Topic): Topic object to be updated
        """
        self._session.add(topic)
        await self._session.flush()

    async def get(self, topic_id: int) -> Topic:
        """
        Get a Topic from the database by id.

        Args:
            topic_id (int): id of the Topic

        Returns:
            Topic: Topic object
        """
        stmt = select(Topic).where(Topic.id == topic_id)
        result = await self._session.execute(stmt)
        return result.scalars().first()

    async def get_by_symbol(self, symbol: str) -> Topic:
        """
        Get a Topic from the database by symbol.

        Args:
            symbol (str): symbol of the Topic

        Returns:
            Topic: Topic object
        """
        stmt = select(Topic).where(Topic.symbol == symbol)
        result = await self._session.execute(stmt)
        return result.scalars().first()

    async def get_all(self) -> list[Topic]:
        """
        Get all Topics from the database.

        Returns:
            List[Topic]: List of Topic objects
        """
        stmt = select(Topic)
        result = await self._session.execute(stmt)
        return result.scalars().all()

    async def delete(self, topic: Topic) -> None:
        """
        Delete a Topic from the database.

        Args:
            topic (Topic): Topic object to be deleted
        """
        await self._session.delete(topic)
        await self._session.flush()
