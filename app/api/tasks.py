from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc

from app.db.models import Task
from app.db.schemas import TaskCreate, TaskUpdate, TaskRead
from app.db.session import get_async_session
from app.db.dependencies import task_by_id


router = APIRouter()


@router.post(
    "/",
    response_model=TaskRead,
    summary="Создать новую задачу",
    description="""
    Создает новую задачу в системе управления задачами.

    **Тело запроса (json):**
    {
      "title": "Купить продукты",
      "description": "Молоко, хлеб, яйца, сыр",
      "status": "CREATED"
    }
    - `title` - название задачи (обязательное поле)
    - `description` - описание задачи (опционально)
    - `status` - статус задачи (опционально). Доступные значения:
        * CREATED - Создана (по умолчанию)
        * IN_PROGRESS - В процессе выполнения
        * COMPLETED - Завершена 

    **Возвращает:**
    - Объект Task (созданная задача с присвоенным UUID и временными метками)

    **Ошибки:**
    - 422: Невалидные данные
    """
)
async def create_task(task: TaskCreate, db: AsyncSession = Depends(get_async_session)):
    new_task = Task(**task.dict())
    db.add(new_task)
    await db.commit()
    await db.refresh(new_task)

    return new_task


@router.get(
    "/{task_id}",
    response_model=TaskRead,
    summary="Получить задачу по ID",
    description="""
    Возвращает задачу по её уникальному идентификатору.

    **Параметры:**
    - `task_id`: UUID задачи

    **Возвращает:**
    - Объект Task с полной информацией

    **Ошибки:**
    - 404: Задача не найдена
    - 500: Неверный формат UUID
    """
)
async def get_task(task: Task = Depends(task_by_id)):
    return task


@router.get(
    "/",
    response_model=list[TaskRead],
    summary="Получить все задачи",
    description="""
    Возвращает список всех задач в системе, отсортированный по времени создания (сначала новые).

    **Возвращает:**
    - Список объектов Task с полной информацией (может быть пустым)

    **Ошибки:**
    - 500: Ошибка подключения к базе данных
    - 503: База данных недоступна или перегружена
    """
)
async def get_all_tasks(db: AsyncSession = Depends(get_async_session)):
    result = await db.execute(
        select(Task).order_by(desc(Task.created_at))
    )

    return result.scalars().all()


@router.put(
    "/{task_id}",
    response_model=TaskRead,
    summary="Изменить задачу",
    description="""
    Позволяет внести изменения в задачу.
    
    **Параметры:**
    - `task_id`: UUID задачи

    **Тело запроса (json):**
    {
      "title": "Купить продукты",
      "description": "Молоко, хлеб, яйца, сыр",
      "status": "IN_PROGRESS"
    }
    Все поля опциональны
    - `title` - название задачи
    - `description` - описание задачи
    - `status` - статус задачи. Доступные значения:
        * CREATED - Создана
        * IN_PROGRESS - В процессе выполнения
        * COMPLETED - Завершена 

    **Возвращает:**
    - Объект Task (скорректированная задача с измененными данными и временной меткой изменения)

    **Ошибки:**
    - 422: Невалидные данные
    - 404: Задача не найдена
    """
)
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


@router.delete(
    "/{task_id}",
    summary="Удалить задачу по ID",
    description="""
    Удаляет задачу из системы по её уникальному идентификатору - без возможности восстановления.

    **Параметры:**
    - `task_id`: UUID задачи

    **Возвращает:**
    объект json: {"message": "Task deleted"}

    **Ошибки:**
    - 404: Задача не найдена
    """
)
async def delete_task(task: Task = Depends(task_by_id), db: AsyncSession = Depends(get_async_session)):
    await db.delete(task)
    await db.commit()

    return {"message": "Task deleted"}
