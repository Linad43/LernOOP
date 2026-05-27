from pathlib import Path

import pytest

from src.model.Category import Category
from src.model.Product import Product


@pytest.fixture
def product_iphone() -> Product:
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


# @pytest.fixture
# def path_json() -> Path:
#     path = Path(__file__).resolve().parents[1]
#     json_path = path / "data" / "products.json"
#     return json_path


def test_init(product_iphone: Product) -> None:
    assert product_iphone.name == "Iphone 15"
    assert product_iphone.description == "512GB, Gray space"
    assert product_iphone.price == 210000.0
    assert product_iphone.quantity == 8


# def test_read_json(path_json: Path) -> None:
#     read_data = Category.read_json(path_json)
#     assert len(read_data) == 2
#     assert read_data[0].name == "Смартфоны"
#     assert (
#         read_data[0].description
#         == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
#     )
#     assert len(read_data[0].products) == 3
