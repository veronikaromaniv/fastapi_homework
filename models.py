from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Director(Base):
    __tablename__ = "directors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    country = Column(String)

    movies = relationship("Movie", back_populates="director_rel")


class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    year = Column(Integer)
    genre = Column(String)
    rating = Column(Float)

    director_id = Column(Integer, ForeignKey("directors.id"))
    director_rel = relationship("Director", back_populates="movies")