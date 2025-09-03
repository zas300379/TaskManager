from typing import cast
from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Task
from app.db.session import get_async_session


async def task_by_id(task_id: str, db: AsyncSession = Depends(get_async_session)) -> Task:
    task = await db.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return cast(Task, task)
