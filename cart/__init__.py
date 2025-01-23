import json
from typing import List

import products
from products import Product

from cart import dao


class Cart:
    def __init__(self, id: int, username: str, contents: List[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    @staticmethod
    def load(data: dict) -> "Cart":
        return Cart(
            id=data["id"],
            username=data["username"],
            contents=[Product(**item) for item in json.loads(data["contents"])],
            cost=data["cost"],
        )


def get_cart(username: str) -> List[Product]:
    cart_details = dao.get_cart(username)
    if not cart_details:
        return []

    all_products = []
    for cart_detail in cart_details:
        try:
            contents = json.loads(cart_detail["contents"])
        except json.JSONDecodeError:
            continue  # Skip invalid JSON contents
        all_products.extend(products.get_product(item) for item in contents)

    return all_products


def add_to_cart(username: str, product_id: int):
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    dao.remove_from_cart(username, product_id)


def delete_cart(username: str):
    dao.delete_cart(username)
