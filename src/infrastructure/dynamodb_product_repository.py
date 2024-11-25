import boto3
from src.domains.product.entities import Product
from src.domains.product.value_objects import Price
from src.ports.product_repository import ProductRepository
from typing import Optional
from decimal import Decimal
from ..config import config

class DynamoDBProductRepository(ProductRepository):
    def __init__(self):
        self.table = boto3.resource("dynamodb").Table(config.database_config.product_table_name)

    def find_by_id(self, product_id: str) -> Optional[Product]:
        response = self.table.get_item(Key={"PK": "product", "SK": product_id})
        item = response.get("Item")
        if item:
            return Product(product_id=item["SK"], name=item["name"], price=Price(value=item["price"]))
        return None

    def save(self, product: Product) -> None:
        self.table.put_item(Item={
            "PK": "product",
            "SK": product.product_id,
            "name": product.name,
            "price": Decimal(product.price.value),
        })