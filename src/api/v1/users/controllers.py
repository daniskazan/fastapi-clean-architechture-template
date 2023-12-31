from fastapi import Request
from fastapi import APIRouter
from fastapi import Depends
from fastapi import status

from api.v1.users.dependencies import get_user_service
from api.v1.users.serializers import UserRegistrationBody

from core.users.exceptions import UserAlreadyExistsError, UserAlreadyExistsHttpException
from core.common.utils.build_generic_response import OkResponse
from core.users.domain import User
from core.users.service import UserService

router = APIRouter(prefix="/users")


@router.post("/", name="users:registration")
async def user_registration(
    request: Request,
    body: UserRegistrationBody,
    user_service: UserService = Depends(get_user_service),
):
    user: User = User(**body.model_dump())
    try:
        user_service.register(user=user)
    except UserAlreadyExistsError:
        raise UserAlreadyExistsHttpException
    return OkResponse.new(status_code=status.HTTP_201_CREATED, data=None)
