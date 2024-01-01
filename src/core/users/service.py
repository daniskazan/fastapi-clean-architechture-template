from api.v1.users.serializers import UserLoginBody
from core.users.domain import User
from core.users.repository import UserRepository
from core.users.exceptions import InvalidCredentialsError
from core.common.security import pwd_context


class UserService:
    def __init__(self, *, repository: UserRepository, ) -> None:
        self.repository: UserRepository = repository

    def register(self, *, user: User):
        registered_user: User = self.repository.create(user=user)
        return registered_user

    def login(self, *, ctx: UserLoginBody) -> User:
        user: User = self.repository.get_by_email(email=ctx.email)
        self.__check_password(user=user, raw_password=ctx.password)
        return user

    @staticmethod
    def __check_password(user: User, raw_password: str):
        h = pwd_context.hash(secret=raw_password)
        user_p = user.password
        the_same: bool = pwd_context.verify(secret=raw_password, hash=user.password)
        if not the_same:
            raise InvalidCredentialsError
