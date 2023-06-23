from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from decimal import Decimal


class ShopDetailsBase(BaseModel):
    seller_id: UUID
    name: str
    description: Optional[str]

class ShopDetailsCreate(ShopDetailsBase):
    pass

class ShopDetails(ShopDetailsBase):
    id: UUID

    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    shop_id: UUID
    name: str
    image_url: str
    description: Optional[str]
    price: Decimal
    currency_id: UUID

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: UUID

    class Config:
        orm_mode = True
