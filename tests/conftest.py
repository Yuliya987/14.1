import pytest

from src.category import Category
from src.product import Product


def category():
    return Category('name', 'description', 'products')


@pytest.fixture
def sample_product():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def multiple_products():
    return [Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
    Product("Test Category", "Test Description", "Test Product", 7),
    Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
            ]


@pytest.fixture
def product1():
    return Product("Test Product", "Test Description", 10.99, 100)


@pytest.fixture
def test_product_data1():
    return {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5}


@pytest.fixture
def test_product_list1():
    return ["Test Product", "Test Description", 10.99, 100]


@pytest.fixture
def test_product_data2():
    return {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 20000.0,
         "quantity": 1}


@pytest.fixture
def test_product_data3():
    return {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 250000.0,
         "quantity": 1}


@pytest.fixture
def price_zero():
    return 0


@pytest.fixture
def price_negative():
    return -100
