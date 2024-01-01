from fastapi.exceptions import HTTPException
from fastapi import status


class TaskNotFoundError(Exception):
    pass


class TaskNotFoundException(HTTPException):
    def __init__(
            self,
            status_code: int = status.HTTP_404_NOT_FOUND,
            detail: str = "Task not found.",
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers={"WWW-Authenticate": "Bearer"})
