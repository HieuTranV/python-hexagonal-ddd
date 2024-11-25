from typing import Protocol, Optional
from src.domains.user.entities import User

class UserRepository(Protocol):
    def find_by_id(self, user_id: str) -> Optional[User]:
        pass

    def save(self, user: User) -> None:
        pass