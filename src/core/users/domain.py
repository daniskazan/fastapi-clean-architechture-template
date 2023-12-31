from uuid import UUID
import datetime as dt

from passlib.context import CryptContext
import uuid_extensions


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User:
    def __init__(
        self, *, username: str, password: str, date_of_birth: dt.date, email: str
    ) -> None:
        self.id: UUID = uuid_extensions.uuid7()
        self.username: str = username
        self.password: str = pwd_context.hash(password)
        self.date_of_birth: dt.date = date_of_birth
        self.email: str = email
