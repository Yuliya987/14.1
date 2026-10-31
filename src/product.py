class Product:
    """ Класс товары"""
    name: str
    description: str
    price: float
    quantity: int


    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls,  product_data: dict, product_list: list):
        name = product_data['name']
        description = product_data ['description']
        price = product_data['price']
        quantity = product_data['quantity']

        for product in product_list:
            if product.name  == name:
                product.quantity += quantity
                product.price = max(product.price, price)
                product.description = description
            return product
    new_product = cls(name=name, price=price, quantity=quantity)
    goods_list.append(new_product)
    return new_product