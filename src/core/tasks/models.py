import uuid

from sqlalchemy import orm

from core.tasks.enums import TaskStatusEnum
from core.common.models.base import BaseORMModel
from core.tasks.domain import Task


class TaskORM(BaseORMModel):
    __tablename__ = "tasks"

    assignee_id: orm.Mapped[uuid.UUID] = orm.mapped_column(nullable=True)
    title: orm.Mapped[str]
    description: orm.Mapped[str]
    status: orm.Mapped[TaskStatusEnum]

    def convert_to_domain(self):
        return Task(
            task_id=self.id,
            assignee_id=self.assignee_id,
            title=self.title,
            description=self.description,
            status=self.status,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    @classmethod
    def build_task_orm_from_domain(cls, *, task: Task) -> "TaskORM":
        return TaskORM(**task.__dict__)
