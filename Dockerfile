FROM python:3.10-slim

WORKDIR /app

# Установка системных зависимостей для PostgreSQL и сборки
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Установка Gauge
RUN wget https://github.com/getgauge/gauge/releases/download/v1.5.4/gauge-1.5.4-linux.x86_64.zip && \
    unzip gauge-1.5.4-linux.x86_64.zip -d /usr/local && \
    rm gauge-1.5.4-linux.x86_64.zip

ENV PATH="/usr/local:${PATH}"

RUN gauge install python

# Копируем зависимости сначала для кэширования
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .


# Expose порт
EXPOSE 8000

# Запуск приложения
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
