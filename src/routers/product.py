from fastapi import APIRouter, HTTPException
from src.application.product_service import ProductService
from src.infrastructure.dynamodb_product_repository import DynamoDBProductRepository
from src.domains.product.entities import Product
from src.domains.product.exceptions import ProductNotFoundError

router = APIRouter(prefix="/products")
product_service = ProductService(DynamoDBProductRepository())

@router.get("/{product_id}", response_model=Product)
def get_product(product_id: str):
    try:
        return product_service.get_product(product_id)
    except ProductNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/", status_code=201)
def create_product(product: Product):
    product_service.create_product(product)
    return {"message": "Product created successfully"}