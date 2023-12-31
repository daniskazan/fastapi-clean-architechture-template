from core.users.domain import User
from core.users.models import UserORM
from core.users.repository import UserRepository


class UserService:
    def __init__(self, *, repository: UserRepository) -> None:
        self.repository: UserRepository = repository

    def register(self, *, user: User):
        registered_user: User = self.repository.create(user=user)
        return registered_user
