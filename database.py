from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DATABASE CONFIGURATION

# URL для підключення до БД
DATABASE_URL = "sqlite:///./movies.db"

# Створюємо engine - фізичне з'єднання з БД
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Фабрика сесій для створення сесій на кожен запит
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Базовий клас для всіх SQLAlchemy моделей
Base = declarative_base()

# DEPENDENCY INJECTION - постачальник БД-сесії

#  Функція-генератор для FastAPI Dependency Injection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()