from fastapi import APIRouter

from api.v1.users.controllers import router as user_router
from api.v1.tasks.controllers import router as task_router

router = APIRouter(prefix="/api/v1")


router.include_router(user_router)
router.include_router(task_router)
