from fastapi import Request
from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi.encoders import jsonable_encoder

from api.v1.users.dependencies import get_user_service
from api.v1.users.serializers import UserRegistrationBody
from api.v1.users.serializers import UserLoginBody

from core.users import exceptions as exc
from core.common.utils.build_generic_response import OkResponse
from core.users.domain import User
from core.users.service import UserService

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", name="users:registration")
async def user_registration(
    request: Request,
    body: UserRegistrationBody,
    user_service: UserService = Depends(get_user_service),
):
    user: User = User(**body.model_dump())
    try:
        user_service.register(user=user)
    except exc.UserAlreadyExistsError:
        raise exc.UserAlreadyExistsHttpException
    return OkResponse.new(status_code=status.HTTP_201_CREATED, data=None)


@router.post("/login", name="users:login")
async def login(
        request: Request,
        body: UserLoginBody,
        user_service: UserService = Depends(get_user_service)
):
    try:
        user: User = user_service.login(ctx=body)
    except (exc.InvalidCredentialsError, exc.UserNotFoundError):
        raise exc.InvalidCredentialsException
    return OkResponse.new(status_code=status.HTTP_200_OK, data=jsonable_encoder(user))