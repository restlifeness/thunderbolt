import uuid

from typing import Annotated
from fastapi import Depends

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from thunderbolt.core.base import AbstractRepository
from thunderbolt.core.session import get_session
from thunderbolt.models import ShopDetails


class ShopDetailsRepository(AbstractRepository):
    """
    Repository class for ShopDetails model

    This class encapsulates the database access for the ShopDetails model. It provides
    functions for adding, getting, and deleting ShopDetails records.
    """

    def __init__(self, session: Annotated[AsyncSession, Depends(get_session)]):
        """
        Initialize the ShopDetailsRepository class.

        Args:
            session (AsyncSession): SQLAlchemy Session for database access
        """
        self._session = session

    async def add(self, shop_details: ShopDetails) -> None:
        """
        Add a new ShopDetails to the database.

        Args:
            shop_details (ShopDetails): ShopDetails object to be added
        """
        self._session.add(shop_details)
        await self._session.flush()

    async def update(self, shop_details: ShopDetails) -> None:
        """
        Update a ShopDetails in the database.

        Args:
            shop_details (ShopDetails): ShopDetails object to be updated
        """
        self._session.add(shop_details)
        await self._session.flush()

    async def get(self, seller_id: uuid.UUID) -> ShopDetails:
        """
        Get a ShopDetails from the database by seller id.

        Args:
            seller_id (uuid.UUID): UUID of the Seller

        Returns:
            ShopDetails: ShopDetails object
        """
        stmt = select(ShopDetails).where(ShopDetails.seller_id == seller_id)
        result = await self._session.execute(stmt)
        return result.scalars().first()

    async def get_all(self) -> list[ShopDetails]:
        """
        Get all ShopDetails from the database.

        Returns:
            List[ShopDetails]: List of ShopDetails objects
        """
        stmt = select(ShopDetails)
        result = await self._session.execute(stmt)
        return result.scalars().all()

    async def delete(self, shop_details: ShopDetails) -> None:
        """
        Delete a ShopDetails from the database.

        Args:
            shop_details (ShopDetails): ShopDetails object to be deleted
        """
        await self._session.delete(shop_details)
        await self._session.flush()
