import pytest

from src.category import Category

def test_init_category(new_category):
    assert new_category.name == "Test Category"
    assert new_category.description == "Test Description"
    assert new_category.products == [1,2,3]
    assert Category.category_count == 1


def test_multiple_categories():
    Category("Category 1", "Desc 1",)
    Category("Category 2", "Desc 2",)
    Category("Category 3", "Desc 3",)
    assert Category.category_count == 3

def test_add_product():
    category = Category("Test Category", "Test Description",)
    product = Product("Test Product", 10.0, 5)  # Создаём фиктивный продукт
    category.add_product(product)
    assert len(category.products) == 1
    assert category.products.name == "Test Product"
    assert Category.product_count == 1

