from pydantic import BaseModel, Field
from typing import Optional, List


# MOVIE SCHEMAS

# Базова схема для фільму - містить поля які є скрізь (і у запиті, і у відповіді)
class MovieBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200, description="Назва фільму")
    year: int = Field(..., ge=1900, le=2100, description="Рік виходу фільму")
    genre: str = Field(..., min_length=1, description="Жанр фільму")
    rating: float = Field(
        ...,
        ge=0.0,
        le=10.0,
        description="Рейтинг від 0.0 до 10.0"
    )
    director_id: int = Field(..., description="ID режисера")

# Схема для створення фільму (клієнт відправляє цей об'єкт у POST/PUT запиті, ID поля немає - БД генерує його сама)
class MovieCreate(MovieBase):
    pass


# Схема для відповіді на запит (містить ID, який генерує БД)
class MovieResponse(MovieBase):
    id: int = Field(..., description="Унікальний ID фільму")

    class Config:
        from_attributes = True  # дозволяє читати з SQLAlchemy ORM об'єктів


# DIRECTOR SCHEMAS

# Базова схема для режисера
class DirectorBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=200, description="Ім'я режисера")
    country: str = Field(..., min_length=1, description="Країна походження")

# Схема для створення режисера
class DirectorCreate(DirectorBase):
    pass

# Схема для відповіді на запит про режисера (включає список його фільмів)
class DirectorResponse(DirectorBase):
    id: int = Field(..., description="Унікальний ID режисера")
    movies: List[MovieResponse] = Field(default_factory=list, description="Всі фільми цього режисера")

    class Config:
        from_attributes = True