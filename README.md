# Task Management API

REST API для управления задачами на FastAPI с PostgreSQL, Docker и автоматическими тестами Gauge.

## Быстрый старт

### Предварительные требования
- Docker Desktop
- Docker Compose
- Git

### Запуск проекта (все платформы)

```bash
# 1. Клонирование репозитория
git clone https://github.com/zas300379/TaskManager.git
cd TaskManager

# 2. Запуск контейнеров
docker-compose up -d --build

# 3. Выполнение миграций БД (обязательно при первом запуске!)
docker-compose exec app alembic upgrade head

# 4. Проверка работы
curl http://localhost:8000/health
# {"status":"healthy"}

# 5. Открыть документацию
# Swagger UI: http://localhost:8000/docs
# ReDoc: http://localhost:8000/redoc
```

## Тестирование

### Запуск тестов Gauge

```bash
# Все тесты
docker-compose exec app gauge run specs/

# Конкретный тестовый файл
docker-compose exec app gauge run specs/01_create_task.spec

# С генерацией отчета
docker-compose exec app gauge run --format html-report specs/
```

## Makefile (только для Linux)

### Настройка на Linux
```bash
# Дать права на выполнение скриптов
chmod +x scripts/*.sh

# Проверить доступные команды
make help
```

### Команды Makefile
```bash
make docker    # Запуск контейнеров
make test      # Запуск тестов
make logs      # Просмотр логов
make stop      # Остановка контейнеров
make clean     # Очистка временных файлов
```
