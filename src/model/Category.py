import json
from pathlib import Path

from src.model.Product import Product


class Category:
    category_count = 0
    product_count = 0

    name: str
    description: str
    products: list[Product]

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products)
        # Возможно следующим образом, не понял задачи
        # Category.product_count += sum(map(lambda product: product.quantity, products))

    def read_json(path: Path) -> list[Category]:
        result = []
        with open(path, encoding="utf-8") as file:
            data = json.load(file)
        for item in data:
            name = item["name"]
            description = item["description"]
            products: list[Product] = []
            for product in item["products"]:
                products.append(
                    Product(product["name"], product["description"], product["price"], product["quantity"])
                )
            result.append(Category(name, description, products))
        return result
