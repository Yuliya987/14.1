from src.product import Product

class Category:
    """ Класс категории товаров"""
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0


    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = []
        Category.category_count += 1
        Category.product_count = len(products)

    def get_product_objects(self):
        return self.__products


    def add_product(self, product):
        self.__products.append(product)
        self.__class__.product_count += 1


        # Геттер для списка товаров
    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            name = product.name
            price = product.price
            quantity = product.quantity
            products_str += f'{name}, {price} руб. Остаток: {quantity} шт.\n'
        return products_str
