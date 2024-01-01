import enum


class TaskStatusEnum(enum.StrEnum):
    IN_PROCESS = "in_process"
    DONE = "done"
    CANCELED = "canceled"
