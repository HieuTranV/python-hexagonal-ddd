from pydantic import BaseModel

class Email(BaseModel):
    value: str

    def __eq__(self, other):
        return self.value == other.value