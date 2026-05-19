from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

#Модель для таблиці 'directors'(представляє режисера в системі)
class Director(Base):
    __tablename__ = "directors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False, index=True)
    country = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Зв'язок з Movie: один режисер -> багато фільмів (cascade='all, delete-orphan' означає: при видаленні режисера видалити й його фільми)
    movies = relationship(
        "Movie",
        back_populates="director_rel",
        cascade="all, delete-orphan",
        foreign_keys="Movie.director_id"
    )

    def __repr__(self):
        return f"<Director(id={self.id}, name='{self.name}', country='{self.country}')>"

# Модель для таблиці 'movies' (представляє фільм в системі)
class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False, index=True)
    year = Column(Integer, nullable=False)
    genre = Column(String(100), nullable=False)
    rating = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Зовнішній ключ на режисера
    director_id = Column(Integer, ForeignKey("directors.id"), nullable=False)

    # Зв'язок з Director: багато фільмів -> один режисер
    director_rel = relationship("Director", back_populates="movies", foreign_keys=[director_id])

    def __repr__(self):
        return f"<Movie(id={self.id}, title='{self.title}', year={self.year}, rating={self.rating})>"