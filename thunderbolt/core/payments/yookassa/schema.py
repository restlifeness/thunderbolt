
"""
This module provides basic types for creating payments in the YooKassa payment system. 

The types defined here correspond to the elements of a payment transaction in YooKassa, 
including the amount, confirmation details, customer details, individual items of a transaction, 
the overall receipt, and the payment details. 

Each class represents a different part of a transaction and is used to structure the data 
according to the requirements of the YooKassa API.

For more information on how to use these types with the YooKassa API, please refer to the API documentation at:
https://yookassa.ru/developers/api#create_payment

"""

from pydantic import BaseModel, Field

from thunderbolt.core.payments import Priceable


class Amount(BaseModel):
    value: float = Field(example=157.99, description='Amount value')
    currency: str = Field(example='RUB', description='Amount currency')


class Confirmation(BaseModel):
    type: str = Field(example='redirect', description='Confirmation type', default='redirect')
    return_url: str = Field(example='https://example.com/return', description='Confirmation return URL')


class CustomerDetails(BaseModel):
    full_name: str = Field(example='Ivan Ivanov', description='Customer full name')
    email: str = Field(example='example@mail.ru', description='Customer email')
    phone: int = Field(example=79999999999, description='Customer phone')
    inn: int = Field(example=123456789012, description='Customer INN')


class Item(BaseModel, Priceable):
    price: float = Field(example=157.99, description='Item price')
    quantity: float = Field(example=1.0, description='Item quantity', default=1.0)
    description: str = Field(example='Item description', description='Item description')


class Reciept(BaseModel):
    customer: CustomerDetails = Field(
        description='Customer details',
        example=CustomerDetails(
            full_name='Ivan Ivanov',
            email='example@mail.ru',
            phone=79999999999,
            inn=123456789012
        )
    )
    items: list[Item] = Field(
        description='Items',
        example=[
            Item(price=157.99, quantity=1.0, description='Item description #1'),
            Item(price=79.99, quantity=0.5, description='Item description #2')
        ]
    )


class PaymentDetails(BaseModel):
    amount: Amount = Field(
        description='Payment amount', 
        example=Amount(value=157.99, currency='RUB')
    )
    confirmation: Confirmation = Field(
        description='Payment confirmation',
        example=Confirmation(type='redirect', return_url='https://example.com/return')
    )
    description: str = Field(example='Payment description', description='Payment description')
    receipt: Reciept = Field(description='Payment receipt')
