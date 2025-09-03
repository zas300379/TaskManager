from uuid import UUID
from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

from app.core import TaskStatus


class TaskCreate(BaseModel):
    title: str
    description: Optional[str]


class TaskUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    status: Optional[TaskStatus]


class TaskRead(BaseModel):
    id: UUID
    title: str
    description: Optional[str]
    status: TaskStatus
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
