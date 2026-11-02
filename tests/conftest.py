import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def new_category():
    return Category("Test Category", "Test Description", "Test Product")


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
