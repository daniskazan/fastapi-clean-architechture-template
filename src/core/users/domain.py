from uuid import UUID
import datetime as dt

import uuid_extensions

from core.common.security import pwd_context


class User:
    def __init__(
        self, *, username: str, password: str, date_of_birth: dt.date, email: str
    ) -> None:
        self.id: UUID = uuid_extensions.uuid7()
        self.username: str = username
        self.password: str = password
        self.date_of_birth: dt.date = date_of_birth
        self.email: str = email
