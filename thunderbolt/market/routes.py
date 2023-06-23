import uuid

from fastapi import APIRouter, Depends, HTTPException, status

# TODO: add __init__ dude
from .repository.shop import ShopDetailsRepository
from .repository.product import ProductRepository

from .schema import ShopDetails, Product


market_router = APIRouter(
    tags=["market"],
    prefix="/market",
)

# BIG TODO: Separate the routes into different files
# For example, all the routes for the shop should be in a file called shop.py

@market_router.get("/users/{seller_id}/shops/", response_model=ShopDetails)
async def get_user_owned_shop(seller_id: uuid.UUID, shop_repo: ShopDetailsRepository = Depends()):
    """
    Get a ShopDetails from the database by seller id.

    Args:
        seller_id (uuid.UUID): UUID of the Seller

    Returns:
        ShopDetails: ShopDetails object
    """
    shop_details = await shop_repo.get(seller_id)
    if not shop_details:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Shop not found")
    return shop_details


@market_router.get("/shops/{shop_id}/products/", response_model=list[Product])
async def get_products_by_shop(
    shop_id: uuid.UUID,
    product_repo: ProductRepository = Depends(),
):
    """
    Get all Products for a specific Shop from the database.

    Args:
        shop_id (uuid.UUID): UUID of the Shop

    Returns:
        List[Product]: List of Product objects
    """
    products = await product_repo.get_all_products_by_shop_id(shop_id)
    if not products:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Products not found")
    return products
