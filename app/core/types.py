from enum import Enum


class TaskStatus(str, Enum):
    CREATED = 'CREATED'
    IN_PROGRESS = 'IN_PROGRESS'
    DONE = 'DONE'
