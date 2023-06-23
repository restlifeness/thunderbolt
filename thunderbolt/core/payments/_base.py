
from typing import Iterable, Protocol
from abc import ABC, abstractmethod


class Priceable(Protocol):
    """
    A protocol that defines a 'price' attribute.
    """
    price: float


class ProductList(list):
    """
    A class that inherits from list with an expectation that each element in the list has a 'price' attribute.
    Raises ValueError if an element without a 'price' attribute is found during initialization.
    """
    def __init__(self, sequence: Iterable[Priceable]):
        for elem in sequence:
            if not hasattr(elem, 'price'):
                raise ValueError("Each element in the sequence should have a 'price' attribute.")
        super().__init__(sequence)

    def total(self):
        """
        Get the total price of all products in the list.
        
        Returns:
            float: The total price of all products in the list.
        """
        return sum([product.price for product in self])


class PaymentSystem(ABC):
    @abstractmethod
    def create_payment(self, amount: float) -> str:
        """
        Create a payment.
        
        Args:
            amount (float): The amount to be paid.
        
        Returns:
            str: The payment id.
        """
        raise NotImplementedError

    @abstractmethod
    def create_payment_by_product_cart(self, product_cart: ProductList) -> str:
        """
        Create a payment by product cart.
        
        Args:
            product_cart (ProductList): The product cart to be used.
        
        Returns:
            str: The payment id.
        """
        raise NotImplementedError
