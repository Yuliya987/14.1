class Product:
    """Класс товары"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict, product_list: list):
        """Метод создает новый товар"""
        name = product_data["name"]
        description = product_data["description"]
        price = product_data["price"]
        quantity = product_data["quantity"]
        for product in product_list:
            if product.name == name:
                product.quantity += quantity
                product.price = max(product.price, price)
                product.description = description
                return product
            else:
                new_product = cls(
                    name=name,
                    description=description,
                    price=price,
                    quantity=quantity
                )
                product_list.append(new_product)
                return new_product

        return product_list

    # Геттер для получения цены
    @property
    def price(self):
        return self.__price

    # Сеттер для проверки на положительное значение новой цены
    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif value < self.__price:
            message = (
                'Цена ниже начальной. Введите "y" для согласия '
                'понизить цену или "n" для отмены: '
            )
            answer = input(message)
            if answer != "y":
                return
        else:
            self.__price = value
