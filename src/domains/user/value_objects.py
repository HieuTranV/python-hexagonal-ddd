from pydantic import BaseModel, EmailStr

class Email(BaseModel):
    value: EmailStr

    def __eq__(self, other):
        return self.value == other.value