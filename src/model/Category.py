from src.model.Product import Product


class Category:
    category_count = 0
    product_count = 0

    name: str
    description: str
    __products: list[Product]

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)
        # Возможно следующим образом, не понял задачи
        # Category.product_count += sum(map(lambda product: product.quantity, products))

    def add_product(self, product: Product) -> None:
        if isinstance(product, Product):
            self.__products.append(product)
        else:
            raise TypeError("Нельзя добавить объекты не наследующиеся от Product")

    @property
    def products(self) -> str:
        result = ""
        for product in self.__products:
            # result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
            result += str(product)
        return result

    def __str__(self) -> str:
        return f"{self.name}, количество продуктов: {sum(product.quantity for product in self.__products)} шт.\n"

    # def read_json(path: Path) -> list[Category]:
    #     result = []
    #     with open(path, encoding="utf-8") as file:
    #         data = json.load(file)
    #     for item in data:
    #         name = item["name"]
    #         description = item["description"]
    #         products: list[Product] = []
    #         for product in item["products"]:
    #             products.append(
    #                 Product(product["name"], product["description"], product["price"], product["quantity"])
    #             )
    #         result.append(Category(name, description, products))
    #     return result
