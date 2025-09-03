from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc

from app.db.models import Task
from app.db.schemas import TaskCreate, TaskUpdate, TaskRead
from app.db.session import get_async_session
from app.db.dependencies import task_by_id


router = APIRouter()


@router.post("/", response_model=TaskRead)
async def create_task(task: TaskCreate, db: AsyncSession = Depends(get_async_session)):
    new_task = Task(**task.dict())
    db.add(new_task)
    await db.commit()
    await db.refresh(new_task)

    return new_task


@router.get("/{task_id}", response_model=TaskRead)
async def get_task(task: Task = Depends(task_by_id)):
    return task


@router.get("/", response_model=list[TaskRead])
async def get_all_tasks(db: AsyncSession = Depends(get_async_session)):
    result = await db.execute(
        select(Task).order_by(desc(Task.created_at))
    )

    return result.scalars().all()


@router.put("/{task_id}", response_model=TaskRead)
async def update_task(
        task_update: TaskUpdate,
        task: Task = Depends(task_by_id),
        db: AsyncSession = Depends(get_async_session)
):
    for key, value in task_update.dict(exclude_unset=True).items():
        setattr(task, key, value)

    await db.commit()
    await db.refresh(task)

    return task


@router.delete("/{task_id}")
async def delete_task(task: Task = Depends(task_by_id), db: AsyncSession = Depends(get_async_session)):
    await db.delete(task)
    await db.commit()

    return {"message": "Task deleted"}
