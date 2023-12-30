from fastapi import Request
from fastapi import APIRouter

from api.v1.users.serializers import UserRegistrationBody
from core.users.domain import User


router = APIRouter(prefix="/users")


@router.post("/", name="users:registration")
async def user_registration(request: Request, body: UserRegistrationBody):
    user: User = User(**body.model_dump())
    return user
