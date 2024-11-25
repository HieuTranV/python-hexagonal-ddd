import pytest
from unittest.mock import MagicMock
from src.application.user_service import UserService
from src.domains.user.entities import User
from src.domains.user.exceptions import UserNotFoundError
from src.domains.user.value_objects import Email

@pytest.fixture
def mock_user_repository():
    return MagicMock()

@pytest.fixture
def user_service(mock_user_repository):
    return UserService(mock_user_repository)

def test_get_user_success(user_service, mock_user_repository):
    """
    Test UserService.get_user successfully returns a user.
    """
    mock_user = User(user_id="123", name="John Doe", email=Email(value="john.doe@example.com"))
    mock_user_repository.find_by_id.return_value = mock_user

    user = user_service.get_user("123")
    assert user == mock_user
    mock_user_repository.find_by_id.assert_called_once_with("123")

def test_get_user_not_found(user_service, mock_user_repository):
    """
    Test UserService.get_user raises an exception when the user is not found.
    """
    mock_user_repository.find_by_id.return_value = None

    with pytest.raises(UserNotFoundError) as excinfo:
        user_service.get_user("nonexistent-id")

    assert "User with ID nonexistent-id not found" in str(excinfo.value)
    mock_user_repository.find_by_id.assert_called_once_with("nonexistent-id")

def test_create_user(user_service, mock_user_repository):
    """
    Test UserService.create_user successfully saves a user.
    """
    mock_user = User(user_id="123", name="John Doe", email=Email(value="john.doe@example.com"))
    
    user_service.create_user(mock_user)
    mock_user_repository.save.assert_called_once_with(mock_user)