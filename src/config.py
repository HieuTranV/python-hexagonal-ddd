from pydantic import BaseModel
import os
class DatabaseConfig(BaseModel):
    user_table_name: str = os.getenv("USER_TABLE_NAME")
    product_table_name: str = os.getenv("PRODUCT_TABLE_NAME")
class Configurations(BaseModel):
    database_config: DatabaseConfig = DatabaseConfig()
config = Configurations()