from importlib.metadata import pass_none


class Product:
    name: str
    description: str
    price: float
    quantity: str


prod_1 = Product()
prod_2 = Product()


class Category:
    name: str
    description: str
    products: str

cat_1 = Category()
cat_2 = Category()
