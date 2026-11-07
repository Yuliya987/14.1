
class Category:
    """ Класс категории товаров"""
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0
    products_list: list = []


    def get_product_objects(self):
        return self.__products


    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count = len(products)
        Category.products_list.extend(products)


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

    @property
    def products_in_list(self) -> list:
        """Геттер, который возвращает приватный атрибут products в виде списка"""
        return self.__products
