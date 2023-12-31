import datetime as dt
from sqlalchemy import orm
from sqlalchemy import types

from core.common.models.base import BaseORMModel
from core.users.domain import User


class UserORM(BaseORMModel):
    __tablename__ = "users"
    username: orm.Mapped[str] = orm.mapped_column(types.String, nullable=False)
    password: orm.Mapped[str] = orm.mapped_column(types.String, nullable=False)
    email: orm.Mapped[str] = orm.mapped_column(
        types.String, nullable=False, unique=True
    )
    date_of_birth: orm.Mapped[dt.date] = orm.mapped_column(types.Date)
    is_superuser: orm.Mapped[bool] = orm.mapped_column(types.Boolean, default=False)

    def convert_to_domain(self):
        return User(
            username=self.username,
            password=self.password,
            email=self.username,
            date_of_birth=self.date_of_birth,
        )

    @classmethod
    def build_user_orm_from_domain(cls, *, user: User) -> "UserORM":
        return UserORM(**user.__dict__)
