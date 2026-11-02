import unittest
from unittest.mock import patch

from src.category import Category
from src.product import Product


def test_init_category(new_category):
    assert new_category.name == "Test Category"
    assert new_category.description == "Test Description"
    assert new_category.products == [1,2,3]
    assert Category.category_count == 1


def test_multiple_categories():
    Category("Category 1", "Desc 1", "Product1")
    Category("Category 2", "Desc 2", "Product2")
    Category("Category 3", "Desc 3", "Product3")
    assert Category.category_count == 3


def test_add_product():
    category = Category("Test Category", "Test Description", 'Test Products')
    product = Product("Test Product", 10.0, 5, 4)
    category.add_product(product)
    assert len(category.products) == 1
    assert category.products.name == "Test Product"
    assert Category.product_count == 1


class TestCategory(unittest.TestCase):
    def test_products_returns_correct_string(self):
        product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        category = Category('name', 'description', 'products')

        mock_products = [product1, product2]

        with patch.object(category, 'products',
            return_value="Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"):
            result = Category.products

        self.assertEqual(result, "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n Iphone 15, 210000.0 руб. Остаток: 8 шт.\n")
        mock_products.assert_called_once()
