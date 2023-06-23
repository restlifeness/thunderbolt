import yookassa

from typing import Iterable, Optional
from yookassa.payment import PaymentResponse

from thunderbolt.core.payments import Priceable, ProductList, PaymentSystem
from thunderbolt.core.payments._base import Priceable, ProductList
from .schema import PaymentDetails, CustomerDetails, Item, Reciept, Amount, Confirmation


class YookassaItem(Priceable):
    name: str


class YookassaProductList(ProductList):
    def __init__(self, sequence: Iterable[YookassaItem]):
        super().__init__(sequence)


class YookassaPaymentSystem(PaymentSystem):
    BASE_CURRENCY = 'RUB'

    def __init__(
        self,
        customer_details: CustomerDetails,
        confirmation_url: str,
        base_currency: Optional[str] = None,
    ) -> None:
        self.customer_details = customer_details
        self.confirmation_url = confirmation_url

        if base_currency:
            self.BASE_CURRENCY = base_currency

    def _convert_product_cart(self, product_cart: ProductList) -> YookassaProductList:
        yookassa_product_cart = list()
        for product in product_cart:
            yookassa_product_cart.append(
                YookassaItem(
                    name=product.name,
                    price=product.price,
                )
            )
        return yookassa_product_cart

    @staticmethod
    def create_payment(payment_details: PaymentDetails) -> PaymentResponse:
        payment = yookassa.Payment.create(
            **payment_details.dict()
        )
        return payment

    def create_payment_by_product_cart(self, product_cart: YookassaProductList) -> PaymentResponse:
        total = product_cart.total()
        reciept = Reciept(
            customer=self.customer_details,
            items=self._convert_product_cart(product_cart),
        )
        confirmation = Confirmation(
            return_url=self.confirmation_url,
        )
        payment_data = PaymentDetails(
            amount=Amount(
                value=total,
                currency=self.BASE_CURRENCY,
            ),
            confirmation=confirmation,
            receipt=reciept,
        )
        return self.create_payment(payment_data)
