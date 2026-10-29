import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def new_category():
    return Category("Test Category", "Test Description", "Test Product")


@pytest.fixture
def new_product():
    return Product("Test Product", "Test Description", 10.99, 100)
