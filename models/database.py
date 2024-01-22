from typing import Optional
from environs import Env
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def load_config(path: Optional[str] = None) -> str:
    env: Env = Env()
    # Добавляем в переменные окружения данные, прочитанные из файла .env
    env.read_env(path)
    
    database=env('DATABASE')
    db_host=env('DB_HOST')
    db_user=env('DB_USER')
    db_password=env('DB_PASSWORD')
    
    return f"postgresql://{db_user}:{db_password}@{db_host}/{database}"


SQLALCHEMY_DATABASE_URL = load_config()


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()