from uuid import UUID

from sqlalchemy import sql
from sqlalchemy import exc
from core.users import exceptions
from core.common.repository.base import Repository
from core.users.models import UserORM
from core.users.domain import User
from core.users.exceptions import UserAlreadyExistsError


class UserRepository(Repository):
    def get_by_uuid(self, *, uuid: UUID) -> User:
        query = sql.select(UserORM).filter_by(id=uuid)
        user_orm = self.db.execute(query)
        try:
            user_orm = user_orm.scalar_one()
        except exc.NoResultFound:
            raise exceptions.UserNotFoundError
        return user_orm.convert_to_domain()

    def create(self, *, user: User) -> User:
        user_orm: UserORM = UserORM.build_user_orm_from_domain(user=user)
        try:

            self.db.add(user_orm)
            self.db.commit()
        except exc.IntegrityError:
            raise UserAlreadyExistsError
        return user

    def update(self, *, user: User):
        return user

    def delete(self, *, user: User):
        return user
