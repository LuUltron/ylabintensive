пример наполнения .env в файле .env.example

Создание виртуального окружения:

python -m venv venv

Запуск виртуального окружения (Windows):

venv/Scripts/activate

Установка недостающих пакетов python в виртуальном окружении:

pip install fastapi, uvicorn, sqlalchemy, psycopg2, environs

Запуск приложения:

uvicorn main:app --reload