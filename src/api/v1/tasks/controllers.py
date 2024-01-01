from uuid import UUID

from fastapi.encoders import jsonable_encoder
from fastapi import Request
from fastapi import APIRouter
from fastapi import Depends
from fastapi import status

from api.v1.tasks.serializers import PublishTaskBody
from api.v1.tasks.dependencies import get_task_service
from core.common.utils.build_generic_response import OkResponse

from core.tasks.domain import Task
from core.tasks.exceptions import TaskNotFoundError, TaskNotFoundException
from core.tasks.service import TaskService

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/{task_id}", name="tasks:get")
async def get_task(
        request: Request,
        task_id: UUID,
        task_service: TaskService = Depends(get_task_service)
):
    try:
        task = task_service.get_task(task_id=task_id)
    except TaskNotFoundError:
        raise TaskNotFoundException
    return OkResponse.new(status_code=status.HTTP_200_OK, data=jsonable_encoder(task))


@router.post("/", name="tasks:create")
async def publish_task(
        request: Request,
        body: PublishTaskBody,
        task_service: TaskService = Depends(get_task_service)
):
    task = Task(**body.model_dump())
    task_service.publish_task(task=task)
    return OkResponse.new(status_code=status.HTTP_201_CREATED, data=jsonable_encoder(task))


@router.delete("/{task_id}", name="tasks:delete")
async def delete_task(
        request: Request,
        task_id: UUID,
        task_service: TaskService = Depends(get_task_service)
):
    try:
        task_service.delete_task(task_id=task_id)
    except TaskNotFoundError:
        raise TaskNotFoundException
    return OkResponse.new(status_code=status.HTTP_204_NO_CONTENT, data=None)