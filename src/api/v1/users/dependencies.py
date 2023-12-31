from core.users.service import UserService
from core.users.repository import UserRepository

from core.common.session import Session


def get_user_service() -> UserService:
    return UserService(repository=UserRepository(db=Session))
