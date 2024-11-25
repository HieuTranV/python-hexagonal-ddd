from pydantic import BaseModel, EmailStr
from .value_objects import Email

class User(BaseModel):
    user_id: str
    name: str
    email: Email

    def update_name(self, new_name: str):
        self.name = new_name