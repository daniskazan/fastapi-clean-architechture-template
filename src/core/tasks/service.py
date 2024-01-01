from dataclasses import dataclass
from uuid import UUID

from core.tasks.domain import Task
from core.tasks.repository import TaskRepository


@dataclass
class TaskService:
    repository: TaskRepository

    def publish_task(
            self,
            *,
            task: Task
    ) -> None:
        self.repository.create(task=task)

    def delete_task(
            self,
            *,
            task_id: UUID
    ) -> None:
        self.repository.delete(task_id=task_id)

    def get_task(
            self,
            *,
            task_id: UUID
    ) -> Task:
        task = self.repository.get_by_uuid(uuid=task_id)
        return task
