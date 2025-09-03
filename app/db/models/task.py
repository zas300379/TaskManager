import uuid

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, DateTime, Enum as SQLEnum
from datetime import datetime, timezone

from app.db.session import Base
from app.core import TaskStatus


class Task(Base):
    __tablename__ = "tasks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    status = Column(SQLEnum(TaskStatus, name='task_status'), default=TaskStatus.CREATED, index=True)
    created_at = Column(DateTime(timezone=True), default=datetime.now(timezone.utc), index=True)
    updated_at = Column(
        DateTime(timezone=True),
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc)
    )
