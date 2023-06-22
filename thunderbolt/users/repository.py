import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from thunderbolt.core.base import AbstractRepository
from thunderbolt.models.user import User


class UserRepository(AbstractRepository):
    """
    Repository class for User model

    This class encapsulates the database access for the User model. It provides
    functions for adding, getting, and deleting user records.
    """

    def __init__(self, session: AsyncSession):
        """
        Initialize the UserRepository class.

        Args:
            session (AsyncSession): SQLAlchemy Session for database access
        """
        self._session = session

    async def add(self, user: User) -> None:
        """
        Add a new User to the database.

        Args:
            user (User): User object to be added
        """
        self._session.add(user)
        await self._session.flush()

    async def update(self, user: User) -> None:
        """
        Update a User in the database.

        Args:
            user (User): User object to be updated
        """
        self._session.add(user)
        await self._session.flush()

    async def get(self, user_id: uuid.UUID) -> User:
        """
        Get a User from the database by id.

        Args:
            user_id (uuid.UUID): UUID of the User

        Returns:
            User: User object
        """
        stmt = select(User).where(User.id == user_id)
        result = await self._session.execute(stmt)
        return result.scalars().first()

    async def get_by_username(self, username: str) -> User:
        """
        Get a User from the database by username.

        Args:
            username (str): username of the User

        Returns:
            User: User object
        """
        stmt = select(User).where(User.username == username)
        result = await self._session.execute(stmt)
        return result.scalars().first()

    async def get_by_email(self, email: str) -> User:
        """
        Get a User from the database by email.

        Args:
            email (str): email of the User

        Returns:
            User: User object
        """
        stmt = select(User).where(User.email == email)
        result = await self._session.execute(stmt)
        return result.scalars().first()

    async def get_all(self) -> list[User]:
        """
        Get all Users from the database.

        Returns:
            List[User]: List of User objects
        """
        stmt = select(User)
        result = await self._session.execute(stmt)
        return result.scalars().all()

    async def delete(self, user: User) -> None:
        """
        Delete a User from the database.

        Args:
            user (User): User object to be deleted
        """
        await self._session.delete(user)
        await self._session.flush()
