from os import access

import pytest
from src.product import Product


def test_init(new_product):
    assert new_product.name == "Test Product"
    assert new_product.description == "Test Description"
    assert new_product.price == 10.99
    assert new_product.quantity == 100
