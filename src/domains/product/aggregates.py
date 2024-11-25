from .entities import Product

class ProductAggregate:
    def __init__(self, product: Product):
        self.product = product