# from pathlib import Path
from unittest.mock import patch

import pytest

# from src.model import product
from src.model.lawnGrass import LawnGrass
from src.model.product import Product
from src.model.smartphone import Smartphone


@pytest.fixture
def product_iphone() -> Product:
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def product_xiaomi() -> Product:
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def smartphone_test() -> Smartphone:
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 0.95, "15", 125, "red")


@pytest.fixture
def lawn_grass_test() -> LawnGrass:
    return LawnGrass("Iphone 15", "512GB, Gray space", 210000.0, 8, "China", 3, "red")


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
    with pytest.raises(ValueError, ) as excinfo:
        Product("Iphone 15", "512GB, Gray space", 210000.0, 0)
    assert str(excinfo.value) == "Товар с нулевым количеством не может быть добавлен"


def test_new_product() -> None:
    product1 = Product.new_product("Iphone 9", "512GB, Gray space", 210000.0, 8)
    product2 = Product.new_product("Iphone 9", "512GB, Gray space", 210000.0, 5)
    assert product1.quantity == 13
    assert product1.quantity == product2.quantity


@patch("builtins.input", return_value="y")
def test_change_price(mock_input, product_iphone: Product) -> None:
    product_iphone.price = 200000.0
    assert product_iphone.price == 200000.0
    product_iphone.price = 220000.0
    assert product_iphone.price == 220000.0


# def test_read_json(path_json: Path) -> None:
#     read_data = Category.read_json(path_json)
#     assert len(read_data) == 2
#     assert read_data[0].name == "Смартфоны"
#     assert (
#         read_data[0].description
#         == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
#     )
#     assert len(read_data[0].products) == 3
def test_sum_products(
        product_iphone: Product, product_xiaomi, smartphone_test: Smartphone, lawn_grass_test: LawnGrass
) -> None:
    assert product_iphone + product_xiaomi == ((210000.0 * 8) + (31000.0 * 14))
    with pytest.raises(TypeError) as excinfo:
        smartphone_test + lawn_grass_test
    assert str(excinfo.value) == "Суммировать можно только объекты одного класса"
    assert smartphone_test + smartphone_test == ((210000.0 * 8) * 2)
