import pytest

from src.product import Product


def test_init_product(product1):
    """Тест на проверку корректности инициализации класса Product"""
    assert product1.name == "Test Product"
    assert product1.description == "Test Description"
    assert product1.price == 10.99
    assert product1.quantity == 100


def test_product_str(product1):
    # Создаём объект с понятными значениями
    product = Product(
        name="Test Product", description="Test Description", price=10.99, quantity=100
    )
    expected = "Test Product, 10.99 руб. Остаток: 100 шт."
    assert str(product) == expected


def test_product_str_with_zero_quantity():
    product = Product(
        name="Наушники", description="Test Description", price=5000.5, quantity=0
    )
    expected = "Наушники, 5000.5 руб. Остаток: 0 шт."
    assert str(product) == expected


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


def test_iter_returns_self(product_iterator):
    """__iter__ должен возвращать сам объект"""
    assert iter(product_iterator) is product_iterator


def test_for_loop_returns_three_products(product_iterator):
    """Цикл for должен отдать ровно три продукта"""
    collected = list(product_iterator)
    assert len(collected) == 3
    assert all(isinstance(p, Product) for p in collected)


def test_next_in_order(product_iterator, category_with_three_products):
    """next() должен отдавать товары строго по порядку"""
    products = category_with_three_products.products_in_list
    assert next(product_iterator) is products[0]
    assert next(product_iterator) is products[1]
    assert next(product_iterator) is products[2]


def test_stop_iteration_after_exhaustion(product_iterator):
    """После прохода по всем элементам должен подниматься StopIteration"""
    for _ in product_iterator:
        pass
    with pytest.raises(StopIteration):
        next(product_iterator)


def test_product_add(first_product, second_product):
    assert first_product + second_product == 50.0


def test_add_product_with_itself(first_product):
    """Сложение товара с самим собой удваивает общую стоимость"""
    assert first_product + first_product == 20.0


def test_add_with_non_product_raises(first_product):
    """При сложении с не-товаром поднимается TypeError"""
    with pytest.raises(TypeError):
        first_product + 10


def test_add_with_string_raises(first_product):
    """Сложение со строкой тоже даёт TypeError"""
    with pytest.raises(TypeError):
        first_product + "не продукт"
