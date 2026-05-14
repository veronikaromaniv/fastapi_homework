from pydantic import BaseModel, Field
from typing import Optional, List

class MovieBase(BaseModel):
    title: str
    year: int
    genre: str
    rating: float = Field(ge=0, le=10) # Рейтинг від 0 до 10
    director_id: int

class MovieCreate(MovieBase):
    pass

class MovieResponse(MovieBase):
    id: int

    class Config:
        from_attributes = True

class DirectorCreate(BaseModel):
    name: str
    country: str

class DirectorResponse(DirectorCreate):
    id: int
    movies: List[MovieResponse] = []

    class Config:
        from_attributes = True