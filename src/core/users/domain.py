from datetime import datetime
from uuid import UUID
from uuid_extensions import uuid7


class User:
    def __init__(
        self, *, username: str, password: str, email: str, date_of_birth: datetime
    ):
        self.id: UUID = uuid7()
        self.username: str = username
        self.password: str = password
        self.date_of_birth: datetime = date_of_birth
        self.email = email
