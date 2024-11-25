from fastapi import APIRouter, HTTPException, Depends
from src.application.user_service import UserService
from src.infrastructure.dynamodb_user_repository import DynamoDBUserRepository
from src.domains.user.entities import User
from src.domains.user.exceptions import UserNotFoundError
from typing import Annotated
router = APIRouter(prefix="/users")
def get_user_service() -> UserService:
    return UserService(DynamoDBUserRepository())

@router.get("/{user_id}", response_model=User)
def get_user(user_id: str, user_service: Annotated[UserService, Depends(get_user_service)]):
    try:
        return user_service.get_user(user_id)
    except UserNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/", status_code=201)
def create_user(user: User, user_service: Annotated[UserService, Depends(get_user_service)]):
    user_service.create_user(user)
    return {"message": "User created successfully"}