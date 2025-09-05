from fastapi import FastAPI
from app.api import tasks


app = FastAPI(
    title="Task Management API",
    description="""
    ## Task Management API
    
    **REST API для управления задачами** с полным CRUD функционалом.
    
    ### Возможности:
    - Создание задач
    - Получение списка задач  
    - Поиск задач по ID
    - Обновление задач
    - Удаление задач
    """)

app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
