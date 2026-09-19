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
        self.products = []
        Category.category_count += 1
        Category.product_count = len(products)

    def add_product(self, product):
        self.products.append(product)