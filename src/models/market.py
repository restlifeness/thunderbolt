
from sqlalchemy import *

from .base import ThunderboltModel


class Currency(ThunderboltModel):
    """
    Currency model
    
    The Currency model represents a currency that is used in the marketplace.
    
    """
    __tablename__ = 'currency'
    
    name = Column(String(3), nullable=False)
    symbol = Column(String(3), nullable=False)


class ShopDetails(ThunderboltModel):
    """
    ShopDetails model
    
    The ShopDetails model represents the details of a shop that is selling products
    in the marketplace.
    
    """
    __tablename__ = 'shop_details'

    seller_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)

    def __repr__(self):
        return f'<ShopDetails {self.seller_name}>'


class Product(ThunderboltModel):
    """
    Product model
    
    The Product model represents a product that is for sale in the marketplace.
    """
    __tablename__ = 'product'

    shop_id = Column(Integer, ForeignKey('shop_details.id'), nullable=False)
    name = Column(String(255), nullable=False)
    image_url = Column(URL, nullable=False)
    description = Column(Text, nullable=True)

    price = Column(DECIMAL, nullable=False)
    currency_id = Column(Integer, ForeignKey('currency.id'), nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'


class ProductCart(ThunderboltModel):
    """
    ProductCart model
    
    The ProductCart model represents a product that is in a user's cart.
    """
    __tablename__ = 'product_cart'

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)

    def __repr__(self):
        return f'<ProductCart {self.user_id} {self.product_id}>'
