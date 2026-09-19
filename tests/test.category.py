import pytest

from src.category import Category

def test_init_category(new_category):
    assert new_category.name == "Test Category"
    assert new_category.description == "Test Description"
    assert new_category.products == [1,2,3]


