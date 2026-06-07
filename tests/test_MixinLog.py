from src.model.product import Product


def test_mixin_log(capsys) -> None:
    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

    captured = capsys.readouterr()

    assert captured.out == (
        "Product('Samsung Galaxy S23 Ultra', " "'256GB, Серый цвет, 200MP камера', " "180000.0, 5)\n"
    )
