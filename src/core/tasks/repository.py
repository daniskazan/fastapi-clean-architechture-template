from uuid import UUID

from core.common.repository.base import Repository, DomainModel
from core.tasks.domain import Task
from core.tasks.exceptions import TaskNotFoundError

from sqlalchemy import sql
from sqlalchemy import exc

from core.tasks.models import TaskORM


class TaskRepository(Repository):

    def get_by_uuid(self, *, uuid: UUID) -> Task:
        query = sql.select(TaskORM).filter_by(id=uuid)
        task_orm = self.db.execute(query)
        try:
            task_orm = task_orm.scalar_one()
        except exc.NoResultFound:
            raise TaskNotFoundError
        return task_orm.convert_to_domain()

    def create(self, *, task: Task) -> None:
        task_orm: TaskORM = TaskORM.build_task_orm_from_domain(task=task)
        self.db.add(task_orm)
        self.db.commit()

    def update(self, *, task: DomainModel) -> None:
        pass

    def delete(self, *, task_id: UUID) -> None:
        query = sql.delete(TaskORM).filter_by(id=task_id)

        self.db.execute(query)
        self.db.commit()
