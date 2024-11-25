from typing import Protocol, Optional
from src.domains.product.entities import Product

class ProductRepository(Protocol):
    def find_by_id(self, product_id: str) -> Optional[Product]:
        pass

    def save(self, product: Product) -> None:
        pass