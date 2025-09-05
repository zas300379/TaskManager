from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from datetime import datetime

from app.core import TaskStatus


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, description="Title must not be empty")
    description: Optional[str]
    status: Optional[TaskStatus]


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(
        None,
        min_length=1,
        description="Title must not be empty if provided"
    )
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
