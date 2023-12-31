from fastapi.exceptions import HTTPException
from fastapi import status

class UserNotFoundError(Exception):
    pass


class UserAlreadyExistsError(Exception):
    pass


class UserAlreadyExistsHttpException(HTTPException):
    def __init__(
            self,
            status_code: int = status.HTTP_400_BAD_REQUEST,
            detail: str = "User already exists.",
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers={"WWW-Authenticate": "Bearer"})


