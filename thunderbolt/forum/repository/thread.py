import uuid

from typing import Annotated
from fastapi import Depends

from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession

from thunderbolt.core.session import get_session
from thunderbolt.core.base import AbstractRepository
from thunderbolt.models import Thread


class ThreadRepository(AbstractRepository):
    """
    Repository class for Thread model

    This class encapsulates the database access for the Thread model. It provides
    functions for adding, getting, and deleting thread records.
    """

    def __init__(self, session: Annotated[AsyncSession, Depends(get_session)]):
        """
        Initialize the ThreadRepository class.

        Args:
            session (AsyncSession): SQLAlchemy Session for database access
        """
        self._session = session

    async def add(self, thread: Thread) -> None:
        """
        Add a new Thread to the database.

        Args:
            thread (Thread): Thread object to be added
        """
        self._session.add(thread)
        await self._session.flush()

    async def update(self, thread: Thread) -> None:
        """
        Update a Thread in the database.

        Args:
            thread (Thread): Thread object to be updated
        """
        self._session.add(thread)
        await self._session.flush()

    async def get(self, thread_id: uuid.UUID) -> Thread:
        """
        Get a Thread from the database by id.

        Args:
            thread_id (uuid.UUID): UUID of the Thread

        Returns:
            Thread: Thread object
        """
        stmt = select(Thread).options(joinedload(Thread.topic)).where(Thread.id == thread_id)
        result = await self._session.execute(stmt)
        return result.scalars().first()

    async def get_all_threads_by_topic(self, topic_id: uuid.UUID) -> list[Thread]:
        """
        Get all Threads for a specific Topic from the database.

        Args:
            topic_id (uuid.UUID): UUID of the Topic

        Returns:
            List[Thread]: List of Thread objects
        """
        stmt = select(Thread).options(joinedload(Thread.topic)).where(Thread.topic_id == topic_id)
        result = await self._session.execute(stmt)
        return result.scalars().all()

    async def get_all(self) -> list[Thread]:
        """
        Get all Threads from the database.

        Returns:
            List[Thread]: List of Thread objects
        """
        stmt = select(Thread).options(joinedload(Thread.topic))
        result = await self._session.execute(stmt)
        return result.scalars().all()

    async def delete(self, thread: Thread) -> None:
        """
        Delete a Thread from the database.

        Args:
            thread (Thread): Thread object to be deleted
        """
        await self._session.delete(thread)
        await self._session.flush()
