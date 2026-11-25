from src.product import Product


def test_init_product(product1):
    """Тест на проверку корректности инициализации класса Product"""
    assert product1.name == "Test Product"
    assert product1.description == "Test Description"
    assert product1.price == 10.99
    assert product1.quantity == 100


def test_absolutely_new_product(test_product_data1, test_product_list1):
    """Тест создания нового продукта, которого нет в списке"""
    new_data = {
        "name": "Iphone 15",
        "description": "512GB, Gray space",
        "price": 210000.0,
        "quantity": 8,
    }
    result = Product.new_product(new_data, test_product_list1)

    assert len(test_product_list1) == 2  # товар добавлен в список
    assert result in test_product_list1
    assert result.name == "Iphone 15"
    assert result.price == 210000.0
    assert result.quantity == 8


def test_new_product_same_price(test_product_data1, test_product_list1):
    """Тест добавления дубликата с той же ценой: количество увеличивается"""
    result = Product.new_product(test_product_data1, test_product_list1)

    assert len(test_product_list1) == 1  # новый товар не создан
    assert result.quantity == 10  # 5 + 5
    assert result.price == 180000.0


def test_new_product_low_price(test_product_data2, test_product_list1):
    """Тест добавления нового продукта, цена которого ниже исходной"""
    result = Product.new_product(test_product_data2, test_product_list1)

    assert len(test_product_list1) == 1
    assert result.quantity == 6  # 5 + 1
    assert result.price == 180000.0


def test_new_product_high_price(test_product_data3, test_product_list1):
    """Тест добавления нового продукта, цена которого выше исходной"""
    result = Product.new_product(test_product_data3, test_product_list1)

    assert len(test_product_list1) == 1
    assert result.quantity == 6
    assert result.price == 250000.0


def test_new_product_empty_list():
    """Тест: при пустом списке метод возвращает сам список (краевой случай)"""
    result = Product.new_product(
        {
         "name": "Тест",
         "description": "Описание",
         "price": 100.0,
         "quantity": 1
         },
        [],
    )
    assert result == []


def test_price_getter(product1):
    """Тест геттера цены"""
    assert product1.price == 10.99


def test_price_zero(price_zero):
    """Тест цена равна нулю"""
    assert "Цена не должна быть нулевая или отрицательная"


def test_price_negative(price_negative):
    """Тест отрицательная цена"""
    assert "Цена не должна быть нулевая или отрицательная"
