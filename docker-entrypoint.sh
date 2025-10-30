#!/bin/bash

HOST="postgres" 
PORT="5432"
USER="postgres"

echo "Ждем, когда будет готов PostgreSQL"
while ! pg_isready -h "$HOST" -p "$PORT" -U "$USER"; do
  echo "PostgreSQL недоступен"
  sleep 1
done

echo "PostgreSQL запущен!"
python -c "from app.database.database import create_db_and_tables; import asyncio; asyncio.run(create_db_and_tables())"

echo "Ввод тестовых данных"
python -m app.seed_data

echo "Запускаем приложение FastAPI"
exec "$@" 