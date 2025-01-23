import json

import products
from products import Product

from cart import dao


class Cart:
    def __init__(self, id: int, username: str, contents: list[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    def load(data):
        return Cart(data["id"], data["username"], data["contents"], data["cost"])


def get_cart(username: str) -> list:
    # Fetch cart details from the DAO
    cart_details = dao.get_cart(username)
    if cart_details is None:
        return []

    # Use list comprehensions to simplify the logic
    items = [
        content
        for cart_detail in cart_details
        for content in eval(cart_detail["contents"])
    ]

    # Fetch products directly using a map function and return the result
    return list(map(products.get_product, items))


def add_to_cart(username: str, product_id: int):
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    dao.remove_from_cart(username, product_id)


def delete_cart(username: str):
    dao.delete_cart(username)
