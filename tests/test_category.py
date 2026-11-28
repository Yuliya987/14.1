import pytest

from src.category import Category
from src.product import Product


def test_init_category(new_category):
    """Тест на проверку корректности инициализации класса Category"""
    assert new_category.name == "Смартфоны"
    assert new_category.description == (
        "Смартфоны, как средство не только коммуникации, " "но и получения дополнительных функций"
    )

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


def test_add_product_success(new_category, smartphone1, lawn_grass1):
    """Можно добавлять и базовый Product, и наследников"""
    new_category.add_product(smartphone1)
    new_category.add_product(lawn_grass1)

    assert len(new_category.products) == 2
    assert Category.product_count == 2


def test_add_product_wrong_type_raises(category):
    """Нельзя добавлять посторонние объекты"""
    with pytest.raises(TypeError):
        category.add_product("просто строка")

    with pytest.raises(TypeError):
        category.add_product(123)

    with pytest.raises(TypeError):
        category.add_product(None)


def test_add_product_class_instead_of_instance_raises(category):
    """Если передать сам класс, а не объект — тоже ошибка"""
    with pytest.raises(TypeError):
        category.add_product(Product)
