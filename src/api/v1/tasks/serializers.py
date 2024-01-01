from uuid import UUID
from pydantic import BaseModel
from pydantic import Field


class PublishTaskBody(BaseModel):
    assignee_id: UUID | None = Field(default=None)
    title: str = Field(..., max_length=128)
    description: str | None = Field(default=None)

