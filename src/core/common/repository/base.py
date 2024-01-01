from typing import TypeVar
from typing import Generic
from typing import Type

from uuid import UUID
from abc import ABC
from abc import abstractmethod

from sqlalchemy.orm import Session


DomainModel = TypeVar("DomainModel")


class Repository(ABC):
    def __init__(self, *, db: Session) -> None:
        self.db: Session = db

    @abstractmethod
    def get_by_uuid(self, *, uuid: UUID) -> DomainModel:
        ...

    @abstractmethod
    def create(self, *, domain_model: DomainModel) -> None:
        ...

    def update(self, *, domain_model: DomainModel) -> None:
        ...

    def delete(self, *, domain_model: DomainModel) -> None:
        ...
