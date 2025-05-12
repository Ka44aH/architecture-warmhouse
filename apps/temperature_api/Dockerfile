# Используем базовый образ Python на базе Alpine
FROM python:3.12-alpine

# Устанавливаем рабочую директорию
WORKDIR /code

# Копируем файлы приложения в контейнер
COPY ./requirements.txt /code/requirements.txt
COPY ./app /code/app

# Устанавливаем зависимости и очищаем кэши
RUN apk add --no-cache gcc musl-dev linux-headers && \
    pip install --no-cache-dir -r /code/requirements.txt && \
    apk del gcc musl-dev linux-headers

# Expose the port the app runs on
EXPOSE 8081

CMD ["uvicorn", "app.main:app", "--port", "8081", "--host", "0.0.0.0"]