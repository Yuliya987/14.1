import pytest

from src.category import Category
from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone
from src.iter_products import IteratorProduct


@pytest.fixture
def new_category():
    """Фикстура новая категория"""
    return Category(
        name="Смартфоны",
        description=(
            "Смартфоны, как средство не только коммуникации, "
            "но и получения дополнительных функций"
        ),
        products=[
            Product(
                "Samsung Galaxy S23 Ultra",
                "256GB, Серый цвет, 200MP камера",
                180000.0,
                5,
            ),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
        ],
    )


@pytest.fixture
def sample_products():
    """Фикстура образцы продуктов"""
    return [
        Product("name1", "description1", 100.0, 5),
        Product("name2", "description2", 200.0, 3),
    ]


@pytest.fixture
def category_with_products(sample_products):
    """Фикстура катоегории с товарами"""
    return Category("name1", "description1", sample_products.copy())


@pytest.fixture
def product1():
    """Фикстура продукт 1"""
    return Product("Test Product", "Test Description", 10.99, 100)


@pytest.fixture
def test_product_data1():
    """Фикстура словарь с продуктами 1"""
    return {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }


@pytest.fixture
def test_product_list1():
    """Фикстура список продуктов 1"""
    return [
        Product(
            "Samsung Galaxy S23 Ultra",
            "256GB, Серый цвет, 200MP камера",
            180000.0,
            5,
        )
    ]


@pytest.fixture
def test_product_data2():
    """Фикстура словарь с продуктами 2"""
    return {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 20000.0,
        "quantity": 1,
    }


@pytest.fixture
def test_product_data3():
    """Фикстура словарь с продуктами 3"""
    return {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 250000.0,
        "quantity": 1,
    }


@pytest.fixture
def price_zero():
    """Фикстура нулевая цена"""
    return 0


@pytest.fixture
def price_negative():
    """Фикстура отрицательная цена"""
    return -100


@pytest.fixture
def category_with_three_products():
    """Фикстура категории с тремя товарами"""
    product1 = Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    description = (
        "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни"
    )
    return Category("Смартфоны", description, [product1, product2, product3])


@pytest.fixture
def first_product():
    return Product("name1", "description1", 10.0, 1)


@pytest.fixture
def second_product():
    return Product("name2", "description2", 20.0, 2)


@pytest.fixture
def product_iterator(category_with_three_products):
    """Итератор по товарам категории"""
    return IteratorProduct(category_with_three_products)


@pytest.fixture
def category():
    """Фикстура пустая категория"""
    return Category(
        name="Пустая категория", description="Тестовая", products=[]
    )


@pytest.fixture
def smartphone1():
    """Фикстура смартфон 1"""
    return Smartphone(
        "Iphone 15",
        "512GB," " Gray space",
        210000.0,
        8,
        98.2,
        "15",
        512,
        "Gray space",
    )


@pytest.fixture
def lawn_grass1():
    """Фикстура газонная трава 1"""
    return LawnGrass(
        name="Газонная трава",
        description="Элитная трава для газона",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="7 дней",
        color="Зелёный",
    )
