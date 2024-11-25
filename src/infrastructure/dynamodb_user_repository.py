import boto3
from src.domains.user.value_objects import Email
from src.domains.user.entities import User
from src.ports.user_repository import UserRepository
from typing import Optional
from ..config import config
from botocore.exceptions import ClientError

class DynamoDBUserRepository(UserRepository):
    def __init__(self):
        self.table = boto3.resource("dynamodb").Table(config.database_config.user_table_name)

    def find_by_id(self, user_id: str) -> Optional[User]:
        try:
            response = self.table.get_item(Key={"PK": "user", "SK": user_id})
            item = response.get("Item")
            if item:
                return User(user_id=item["SK"], name=item["name"], email=Email(value=item["email"]))
            return None
        except ClientError as e:
            raise Exception(f"Failed to fetch user from DynamoDB: {str(e)}")

    def save(self, user: User) -> None:
        self.table.put_item(Item={
         "PK": "user",
         "SK": user.user_id,
         "name": user.name,
         "email": user.email.value   
        })