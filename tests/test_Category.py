import pytest

from src.model.Category import Category
from src.model.product import Product


@pytest.fixture
def category_smart() -> Category:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )


def test_category(category_smart: Category) -> None:
    assert category_smart.name == "Смартфоны"
    assert (
            category_smart.description
            == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )


def test_products(category_smart: Category) -> None:
    category_smart.add_product(Product("Samsung Galaxy S23", "256GB, Серый цвет, 200MP камера", 100000.0, 1))
    assert category_smart.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
        "Samsung Galaxy S23, 100000.0 руб. Остаток: 1 шт.\n"
    )


def test_category_toString(category_smart: Category) -> None:
    assert str(category_smart) == "Смартфоны, количество продуктов: 27 шт.\n"
