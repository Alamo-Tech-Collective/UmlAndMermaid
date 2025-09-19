from datetime import datetime
from typing import List, Optional


class Product:
    def __init__(self, product_id: int, name: str, price: float):
        self._id = product_id
        self._name = name
        self._price = price

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> float:
        return self._price

    def update_price(self, new_price: float) -> None:
        if new_price < 0:
            raise ValueError("Price cannot be negative")
        self._price = new_price


class Order:
    def __init__(self, order_id: int):
        self._id = order_id
        self._date = datetime.now()
        self._status = "pending"
        self._products: List[tuple[Product, int]] = []

    @property
    def id(self) -> int:
        return self._id

    @property
    def date(self) -> datetime:
        return self._date

    @property
    def status(self) -> str:
        return self._status

    def add_product(self, product: Product, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        self._products.append((product, quantity))

    def calculate_total(self) -> float:
        total = 0.0
        for product, quantity in self._products:
            total += product.price * quantity
        return total

    def mark_shipped(self) -> None:
        if self._status == "pending":
            self._status = "shipped"
        else:
            raise ValueError(f"Cannot ship order with status: {self._status}")


class Customer:
    def __init__(self, customer_id: int, name: str, email: str):
        self._id = customer_id
        self._name = name
        self._email = email
        self._orders: List[Order] = []

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def email(self) -> str:
        return self._email

    @property
    def orders(self) -> List[Order]:
        return self._orders

    def place_order(self, product: Product, quantity: int) -> Order:
        order_id = len(self._orders) + 1
        order = Order(order_id)
        order.add_product(product, quantity)
        self._orders.append(order)
        return order