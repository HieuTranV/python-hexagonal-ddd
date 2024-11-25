from pydantic import BaseModel
from .value_objects import Price

class Product(BaseModel):
    product_id: str
    name: str
    price: Price

    def update_price(self, new_price: Price):
        self.price = new_price