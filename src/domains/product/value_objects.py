from pydantic import BaseModel

class Price(BaseModel):
    value: float

    def __eq__(self, other):
        return self.value == other.value