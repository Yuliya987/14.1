import unittest
from unittest.mock import patch
from src.product import Product


def test_init_product(product1):
    assert product1.name == "Test Product"
    assert product1.description == "Test Description"
    assert product1.price == 10.99
    assert product1.quantity == 100


def test_absolutely_new_product(test_product_data1, test_product_list1):
    assert [Product("Test Product", "Test Description", 10.99, 100), Product("Samsung Galaxy S23 Ultra",  "256GB, Серый цвет, 200MP камера",  180000.0,
          5)]

def test_new_product_low_price(test_product_data2, test_product_list1):
    assert [Product("Samsung Galaxy S23 Ultra",  "256GB, Серый цвет, 200MP камера",  180000.0,
          5)]

def test_new_product_high_price(test_product_data3, test_product_list1):
    assert [Product("Samsung Galaxy S23 Ultra",  "256GB, Серый цвет, 200MP камера",  250000.0,
          5)]


def test_price_zero(price_zero):
    assert 'Цена не должна быть нулевая или отрицательная'


def test_price_negative(price_negative):
    assert 'Цена не должна быть нулевая или отрицательная'


class TestProductPriceSetter(unittest.TestCase):
    @patch('builtins.input')
    def test_price_setter_when_price_lower_and_user_agrees(self, mock_input):
        mock_input.return_value = 'y'
        product = Product(180000)  # Начальная цена
        product.price = 800  # Попытка снизить цену
        self.assertEqual(product.price, 800)


    @patch('builtins.input')
    def test_price_setter_when_price_lower_and_user_declines(self, mock_input):
        # Настройка теста: что вводить и какой ожидается результат
        mock_input.return_value = 'n'
        product = Product(180000)  # Начальная цена 100
        product.price = 800  # Попытка снизить цену
        self.assertEqual(product.price, 180000)
