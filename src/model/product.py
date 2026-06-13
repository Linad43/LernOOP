from src.model.baseProduct import BaseProduct
from src.model.mixinLog import MixinLog


class Product(MixinLog, BaseProduct):
    products: dict[str, Product] = {}

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.products[name] = self
        super().__init__(name, description, price, quantity)

    @classmethod
    def new_product(cls, name: str, description: str, price: float, quantity: int) -> Product:
        if name in cls.products:
            product = cls.products[name]
            product.quantity += quantity
            return product
        return Product(name, description, price, quantity)

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        if price > 0:
            if self.__price > price:
                choice = input("Цена товара снизилась, вы уверены?(y/n)")
                if choice == "y":
                    self.__price = price
            else:
                self.__price = price

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.\n"

    def __add__(self, other: Product) -> float:
        if type(self) == type(other):
            return (self.__price * self.quantity) + (other.__price * other.quantity)
        else:
            raise TypeError("Суммировать можно только объекты одного класса")

    def __repr__(self) -> str:
        return f"Product('{self.name}', " f"'{self.description}', " f"{self.price}, " f"{self.quantity})"
