from src.product import Product


def test_init_product(product1):
    """Тест на проверку корректности инициализации класса Product"""
    assert product1.name == "Test Product"
    assert product1.description == "Test Description"
    assert product1.price == 10.99
    assert product1.quantity == 100


def test_absolutely_new_product(test_product_data1, test_product_list1):
    """Тест создания нового продукта, которого нет в списке"""
    assert [
        Product("Test Product", "Test Description", 10.99, 100),
        Product(
            "Samsung Galaxy S23 Ultra",
            "256GB, Серый цвет, 200MP камера",
            180000.0,
            5
        ),
    ]


def test_new_product_low_price(test_product_data2, test_product_list1):
    """Тест добавления нового продукта, цена которого ниже исходной"""
    assert [
        Product(
            "Samsung Galaxy S23 Ultra",
            "256GB, Серый цвет, 200MP камера",
            180000.0,
            5
        )
    ]


def test_new_product_high_price(test_product_data3, test_product_list1):
    """Тест добавления нового продукта, цена которого выше исходной"""
    assert [
        Product(
            "Samsung Galaxy S23 Ultra",
            "256GB, Серый цвет, 200MP камера",
            250000.0,
            5
        )
    ]


def test_price_zero(price_zero):
    """Тест цена равна нулю"""
    assert "Цена не должна быть нулевая или отрицательная"


def test_price_negative(price_negative):
    """Тест отрицательная цена"""
    assert "Цена не должна быть нулевая или отрицательная"
