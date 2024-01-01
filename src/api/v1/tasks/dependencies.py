from core.tasks.service import TaskService
from core.tasks.repository import TaskRepository

from core.common.session import Session


def get_task_service() -> TaskService:
    return TaskService(repository=TaskRepository(db=Session))
