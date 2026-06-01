import pytest

from src.model.LawnGrass import LawnGrass


@pytest.fixture
def lawnGrass_test() -> LawnGrass:
    return LawnGrass(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8,
        "China",
        3,
        "red")


def test_init(lawnGrass_test: LawnGrass) -> None:
    assert lawnGrass_test.name == "Iphone 15"
    assert lawnGrass_test.description == "512GB, Gray space"
    assert lawnGrass_test.price == 210000.0
    assert lawnGrass_test.quantity == 8
    assert lawnGrass_test.country == "China"
    assert lawnGrass_test.germination_period == 3
    assert lawnGrass_test.color == "red"

