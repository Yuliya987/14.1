from src.category import Category


def test_init_category(new_category):
    assert new_category.name == "Смартфоны"
    assert new_category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций"
    assert len(new_category.products_in_list) == 3
    assert Category.category_count == 1


def test_get_product_objects_empty(category):
    """Геттер возвращает пустой список, если товаров нет."""
    assert category.get_product_objects() == []


def test_add_product_updates_list(category, sample_product):
    """Добавление товара обновляет внутренний список."""
    category.add_product(sample_product)
    products = category.get_product_objects()
    assert len(products) == 1
    assert products[0] is sample_product


def test_add_multiple_products(category, multiple_products):
    """Можно добавить несколько товаров, они сохраняются в порядке добавления."""
    for p in multiple_products:
        category.add_product(p)

        products = category.get_product_objects()
        assert len(products) == len(multiple_products)
        assert all(p1 is p2 for p1, p2 in zip(products, multiple_products))


def test_products_property_empty(category):
    """Если товаров нет, products возвращает пустую строку."""
    assert category.products == ""


def test_products_property_single_product(category, sample_product):
    """Строковое представление для одного товара соответствует формату."""
    category.add_product(sample_product)
    expected = "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт. \n"
    assert category.products == expected


def test_products_property_multiple_products(category, multiple_products):
    """Строковое представление корректно формирует список товаров."""
    for p in multiple_products:
        category.add_product(p)

    expected_lines = [
        f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт.\n"
        for p in multiple_products
    ]
    expected = "".join(expected_lines)


    assert category.products == expected
