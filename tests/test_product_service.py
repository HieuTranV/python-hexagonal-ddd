import pytest
from unittest.mock import MagicMock
from src.application.product_service import ProductService
from src.domains.product.entities import Product
from src.domains.product.exceptions import ProductNotFoundError
from src.domains.product.value_objects import Price

@pytest.fixture
def mock_product_repository():
    return MagicMock()

@pytest.fixture
def product_service(mock_product_repository):
    return ProductService(mock_product_repository)

def test_get_product_success(product_service, mock_product_repository):
    """
    Test ProductService.get_product successfully returns a product.
    """

    mock_product = Product(product_id="123", name="Product 1", price=Price(value=100))
    mock_product_repository.find_by_id.return_value = mock_product
    product = product_service.get_product("123")
    assert product == mock_product
    mock_product_repository.find_by_id.assert_called_once_with("123")

def test_create_product(product_service, mock_product_repository):
    """
    Test ProductService.create_product successfully saves a product.
    """
    mock_product = Product(product_id="123", name="Product 1", price=Price(value=100))
    
    product_service.create_product(mock_product)
    mock_product_repository.save.assert_called_once_with(mock_product)