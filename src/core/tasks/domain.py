import datetime as dt
from uuid import UUID
import uuid_extensions

from core.tasks.enums import TaskStatusEnum


class Task:
    def __init__(
            self,
            *,
            task_id: UUID = uuid_extensions.uuid7(),
            assignee_id: UUID | None = None,
            title: str,
            description: str | None = None,
            status: TaskStatusEnum = TaskStatusEnum.IN_PROCESS,
            created_at: dt.date = dt.datetime.now(tz=dt.UTC),
            updated_at: dt.date = dt.datetime.now(tz=dt.UTC)
    ):
        self.id = task_id
        self.assignee_id = assignee_id
        self.title = title
        self.description = description
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

    def change_status(self, *, to_status: TaskStatusEnum):
        self.status = to_status

    def assign_user_to_task(self, *, assignee_id: UUID):
        self.assignee_id = assignee_id

    def __str__(self):
        return f"<Task UUID: {self.id}, DESCRIPTION: {self.description or 'empty'}>"
