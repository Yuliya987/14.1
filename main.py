from importlib.metadata import pass_none


class Product:
    name: str
    description: str
    price: float
    quantity: str

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

prod_1 = Product()
prod_2 = Product()


class Category:
    name: str
    description: str
    products: str

    def __init__(self):

cat_1 = Category()
cat_2 = Category()
