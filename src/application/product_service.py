from src.ports.product_repository import ProductRepository
from src.domains.product.entities import Product
from src.domains.product.exceptions import ProductNotFoundError
from src.infrastructure.logging.logging_adapter import get_logger
logger = get_logger()

class ProductService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def get_product(self, product_id: str) -> Product:
        product = self.product_repository.find_by_id(product_id)
        if not product:
            raise ProductNotFoundError(f"Product with ID {product_id} not found")
        logger.info(f"Found product with ID {product_id}")
        return product

    def create_product(self, product: Product):
        self.product_repository.save(product)