import uuid

from typing import Annotated
from fastapi import Depends

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from thunderbolt.core.session import get_session
from thunderbolt.core.base import AbstractRepository
from thunderbolt.models import Post


class PostRepository(AbstractRepository):
    """
    Repository class for Post model

    This class encapsulates the database access for the Post model. It provides
    functions for adding, getting, and deleting post records.
    """

    def __init__(self, session: Annotated[AsyncSession, Depends(get_session)]):
        """
        Initialize the PostRepository class.

        Args:
            session (AsyncSession): SQLAlchemy Session for database access
        """
        self._session = session

    async def add(self, post: Post) -> None:
        """
        Add a new Post to the database.

        Args:
            post (Post): Post object to be added
        """
        self._session.add(post)
        await self._session.flush()

    async def update(self, post: Post) -> None:
        """
        Update a Post in the database.

        Args:
            post (Post): Post object to be updated
        """
        self._session.add(post)
        await self._session.flush()

    async def get(self, post_id: uuid.UUID) -> Post:
        """
        Get a Post from the database by id.

        Args:
            post_id (uuid.UUID): UUID of the Post

        Returns:
            Post: Post object
        """
        stmt = select(Post).where(Post.id == post_id).options(joinedload(Post.thread), joinedload(Post.user))
        result = await self._session.execute(stmt)
        return result.scalars().first()

    async def get_by_thread(self, thread_id: uuid.UUID) -> list[Post]:
        """
        Get all Posts for a specific Thread from the database.

        Args:
            thread_id (uuid.UUID): UUID of the Thread

        Returns:
            List[Post]: List of Post objects
        """
        stmt = select(Post).where(Post.thread_id == thread_id).options(joinedload(Post.thread), joinedload(Post.user))
        result = await self._session.execute(stmt)
        return result.scalars().all()

    async def get_by_user(self, user_id: uuid.UUID) -> list[Post]:
        """
        Get all Posts by a specific User from the database.

        Args:
            user_id (uuid.UUID): UUID of the User

        Returns:
            List[Post]: List of Post objects
        """
        stmt = select(Post).where(Post.user_id == user_id).options(joinedload(Post.thread), joinedload(Post.user))
        result = await self._session.execute(stmt)
        return result.scalars().all()

    async def get_all(self) -> list[Post]:
        """
        Get all Posts from the database.

        Returns:
            List[Post]: List of Post objects
        """
        stmt = select(Post).options(joinedload(Post.thread), joinedload(Post.user))
        result = await self._session.execute(stmt)
        return result.scalars().all()

    async def delete(self, post: Post) -> None:
        """
        Delete a Post from the database.

        Args:
            post (Post): Post object to be deleted
        """
        await self._session.delete(post)
        await self._session.flush()
