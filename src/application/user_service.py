from src.ports.user_repository import UserRepository
from src.domains.user.entities import User
from src.domains.user.exceptions import UserNotFoundError
from src.infrastructure.logging.logging_adapter import get_logger
logger = get_logger()
class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_user(self, user_id: str) -> User:
        user = self.user_repository.find_by_id(user_id)
        if not user:
            logger.warning(f"User with ID {user_id} not found")
            raise UserNotFoundError(f"User with ID {user_id} not found")
        logger.info(f"Found user with ID {user_id}")
        return user

    def create_user(self, user: User):
        logger.info(f"Creating user with ID {user.user_id}")
        self.user_repository.save(user)