import pytest

from src.model.smartphone import Smartphone


@pytest.fixture
def smartphone_iphone() -> Smartphone:
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 0.95, "15", 125, "red")


def test_init(smartphone_iphone: Smartphone) -> None:
    assert smartphone_iphone.name == "Iphone 15"
    assert smartphone_iphone.description == "512GB, Gray space"
    assert smartphone_iphone.price == 210000.0
    assert smartphone_iphone.quantity == 8
    assert smartphone_iphone.efficiency == 0.95
    assert smartphone_iphone.model == "15"
    assert smartphone_iphone.memory == 125
    assert smartphone_iphone.color == "red"
