from datetime import datetime
from typing import List, Optional


class Product:
    def __init__(self, product_id: int, name: str, price: float):
        self.id = product_id
        self.name = name
        self.price = price

    def update_price(self, new_price: float) -> None:
        if new_price < 0:
            raise ValueError("Price cannot be negative")
        self.price = new_price


class Order:
    def __init__(self, order_id: int):
        self.id = order_id
        self.date = datetime.now()
        self.status = "pending"
        self.products: List[tuple[Product, int]] = []

    def add_product(self, product: Product, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        self.products.append((product, quantity))

    def calculate_total(self) -> float:
        total = 0.0
        for product, quantity in self.products:
            total += product.price * quantity
        return total

    def mark_shipped(self) -> None:
        if self.status == "pending":
            self.status = "shipped"
        else:
            raise ValueError(f"Cannot ship order with status: {self.status}")


class Customer:
    def __init__(self, customer_id: int, name: str, email: str):
        self.id = customer_id
        self.name = name
        self.email = email
        self.orders: List[Order] = []

    def place_order(self, product: Product, quantity: int) -> Order:
        order_id = len(self.orders) + 1
        order = Order(order_id)
        order.add_product(product, quantity)
        self.orders.append(order)
        return order