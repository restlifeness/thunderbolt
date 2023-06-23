import uuid

from typing import Annotated
from fastapi import Depends

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from thunderbolt.core.base import AbstractRepository
from thunderbolt.core.session import get_session
from thunderbolt.models import Product


class ProductRepository(AbstractRepository):
    """
    Repository class for Product model

    This class encapsulates the database access for the Product model. It provides
    functions for adding, getting, and deleting product records.
    """

    def __init__(self, session: Annotated[AsyncSession, Depends(get_session)]):
        """
        Initialize the ProductRepository class.

        Args:
            session (AsyncSession): SQLAlchemy Session for database access
        """
        self._session = session

    async def add(self, product: Product) -> None:
        """
        Add a new Product to the database.

        Args:
            product (Product): Product object to be added
        """
        self._session.add(product)
        await self._session.flush()

    async def update(self, product: Product) -> None:
        """
        Update a Product in the database.

        Args:
            product (Product): Product object to be updated
        """
        self._session.add(product)
        await self._session.flush()

    async def get(self, product_id: uuid.UUID) -> Product:
        """
        Get a Product from the database by id.

        Args:
            product_id (uuid.UUID): UUID of the Product

        Returns:
            Product: Product object
        """
        stmt = select(Product).where(Product.id == product_id)
        result = await self._session.execute(stmt)
        return result.scalars().first()

    async def get_all_by_user(self, user_id: uuid.UUID) -> list[Product]:
        """
        Get all Products for a specific User from the database.

        Args:
            user_id (uuid.UUID): UUID of the User

        Returns:
            List[Product]: List of Product objects
        """
        stmt = select(Product).where(Product.user_id == user_id)
        result = await self._session.execute(stmt)
        return result.scalars().all()

    async def get_all_products_by_shop_id(self, shop_id: uuid.UUID) -> list[Product]:
        """
        Get all Products for a specific Shop from the database.

        Args:
            shop_id (uuid.UUID): UUID of the Shop

        Returns:
            List[Product]: List of Product objects
        """
        stmt = select(Product).where(Product.shop_id == shop_id)
        result = await self._session.execute(stmt)
        return result.scalars().all()


    async def get_all(self) -> list[Product]:
        """
        Get all Products from the database.

        Returns:
            List[Product]: List of Product objects
        """
        stmt = select(Product)
        result = await self._session.execute(stmt)
        return result.scalars().all()

    async def delete(self, product: Product) -> None:
        """
        Delete a Product from the database.

        Args:
            product (Product): Product object to be deleted
        """
        await self._session.delete(product)
        await self._session.flush()
