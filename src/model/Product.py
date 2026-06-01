class Product:
    products = {}

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(
            self,
            name: str,
            description: str,
            price: float,
            quantity: int
    ) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.products[name] = self

    @classmethod
    def new_product(
            cls,
            name: str,
            description: str,
            price: float,
            quantity: int
    ) -> Product:
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

    def __add__(self, other) -> float:
        if type(self) == type(other):
            return (self.__price * self.quantity) + (other.__price * other.quantity)
        else:
            raise TypeError("Суммировать можно только объекты одного класса")
