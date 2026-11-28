import pytest

from src.product import Product


def test_init_product(product1):
    """Тест на проверку корректности инициализации класса Product"""
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет"
    assert product1.price == 180000.0
    assert product1.quantity == 5


def test_price_setter_lower_price_confirmed(product1, monkeypatch):
    """Понижение цены с подтверждением 'y' — цена меняется"""
    monkeypatch.setattr("builtins.input", lambda _: "y")
    product1.price = 150000.0
    assert product1.price == 150000.0


def test_price_setter_lower_price_declined(product1, monkeypatch):
    """Понижение цены при отказе 'n' — цена не меняется"""
    monkeypatch.setattr("builtins.input", lambda _: "n")
    product1.price = 150000.0
    assert product1.price == 180000.0


def test_price_setter_zero_rejected(product1, capsys):
    """Нулевая цена через сеттер отклоняется с сообщением"""
    product1.price = 0
    assert product1.price == 180000.0

    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_price_setter_negative_rejected(product1, capsys):
    """Отрицательная цена через сеттер отклоняется с сообщением"""
    product1.price = -100.0
    assert product1.price == 180000.0

    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_product_str_with_zero_quantity():
    product = Product(
        name="Наушники",
        description="Test Description",
        price=5000.5,
        quantity=0,
    )
    expected = "Наушники, 5000.5 руб. Остаток: 0 шт."
    assert str(product) == expected


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


def test_product_add(first_product, second_product):
    assert first_product + second_product == 50.0


def test_add_product_with_itself(first_product):
    """Сложение товара с самим собой удваивает общую стоимость"""
    assert first_product + first_product == 20.0


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


def test_add_with_non_product_raises(first_product):
    """При сложении с не-товаром поднимается TypeError"""
    with pytest.raises(TypeError):
        _ = first_product + 10


def test_add_with_string_raises(first_product):
    """Сложение со строкой тоже даёт TypeError"""
    with pytest.raises(TypeError):
        _ = first_product + "не продукт"


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
            "quantity": 1,
        },
        [],
    )
    assert result == []


def test_price_getter(product1):
    """Тест геттера цены"""
    assert product1.price == 180000.0


def test_price_zero(price_zero):
    """Тест цена равна нулю"""
    assert "Цена не должна быть нулевая или отрицательная"


def test_price_negative(price_negative):
    """Тест отрицательная цена"""
    assert "Цена не должна быть нулевая или отрицательная"
