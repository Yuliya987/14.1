class Product:
    """ Класс товары"""
    name: str
    description: str
    price: float
    quantity: int


    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
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
            else:
               new_product = cls(name=name, description = description, price=price, quantity=quantity)
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
            print('Цена не должна быть нулевая или отрицательная')
        elif value < self.__price:
            answer = input('Цена ниже начальной. Введите "y" для согласия понизить цену или "n" для отмены: ')
            if answer == 'y':
                self.__price = value
            else:
                self.__price = self.__price
        else:
            self.__price = value
