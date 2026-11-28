from src.product import Product
from src.iter_products import IteratorProduct


class Category:
    """Класс категории товаров"""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """Метод для инициализации экземпляра класса"""
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        """Возвращает строку с товаром"""
        total_q = sum(
            product.quantity
            for product in self.products_in_list
        )
        return f"{self.name}, количество продуктов: {total_q} шт."

    # Геттер для списка товаров
    @property
    def products(self) -> str:
        product_str = ""
        for product in self.__products:
            product_str += (
                f"{product.name}, {product.price} руб. "
                f"Остаток: {product.quantity} шт.\n"
            )
        return product_str

    def __iter__(self):
        """Возвращает итератор по товарам категории"""
        return IteratorProduct(self)

    def add_product(self, product: Product) -> None:
        """Метод добавляет товар в категорию"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError(
                "В категорию можно добавлять только объекты класса Product "
                "и его наследников"
            )

    @property
    def products_in_list(self):
        return self.__products
