from src.category import Category


def test_init_category(new_category):
    assert new_category.name == "Смартфоны"
    assert new_category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций"

    assert len(new_category.products_in_list) == 3
    assert Category.category_count == 1


def test_category_products_property(category_with_products, sample_products):
    """Проверка корректности форматирования строки с товарами"""

    products_str = category_with_products.products
    expected_lines = [
        f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in sample_products
    ]
    expected = "\n".join(expected_lines) + "\n"
    assert products_str == expected


def test_category_str(category_with_products):
    assert str(category_with_products) == 'name1, количество продуктов: 8 шт.'
