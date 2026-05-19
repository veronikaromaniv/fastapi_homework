from sqlalchemy.orm import Session
import models, schemas



# MOVIE CRUD OPERATIONS

# Отримати список фільмів з пагінацією
def get_movies(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Movie).offset(skip).limit(limit).all()

#  Отримати один фільм за ID або None
def get_movie(db: Session, movie_id: int):
    return db.query(models.Movie).filter(models.Movie.id == movie_id).first()

#  Створити новий фільм (приймає Pydantic схему MovieCreate, ровертає SQLAlchemy об'єкт Movie з ID)
def create_movie(db: Session, movie: schemas.MovieCreate):
    db_movie = models.Movie(**movie.model_dump())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

# Оновити існуючий фільм (повертає оновлений об'єкт або None якщо не знайдено)
def update_movie(db: Session, movie_id: int, movie_data: schemas.MovieCreate):
    db_movie = get_movie(db, movie_id)
    if db_movie:
        for key, value in movie_data.model_dump().items():
            setattr(db_movie, key, value)
        db.commit()
        db.refresh(db_movie)
    return db_movie

# Видалити фільм за ID (повертає True якщо видалено, False якщо не знайдено)
def delete_movie(db: Session, movie_id: int):
    db_movie = get_movie(db, movie_id)
    if db_movie:
        db.delete(db_movie)
        db.commit()
        return True
    return False



# DIRECTOR CRUD OPERATIONS

# Отримати список режисерів з пагінацією
def get_directors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Director).offset(skip).limit(limit).all()

# Отримати одного режисера за ID або None.
def get_director(db: Session, director_id: int):
    return db.query(models.Director).filter(models.Director.id == director_id).first()

# Створити нового режисера
def create_director(db: Session, director: schemas.DirectorCreate):
    db_director = models.Director(**director.model_dump())
    db.add(db_director)
    db.commit()
    db.refresh(db_director)
    return db_director

#   Оновити існуючого режисера
def update_director(db: Session, director_id: int, director_data: schemas.DirectorCreate):
    db_director = get_director(db, director_id)
    if db_director:
        for key, value in director_data.model_dump().items():
            setattr(db_director, key, value)
        db.commit()
        db.refresh(db_director)
    return db_director

# Видалити режисера (також видалить всі його фільми (CASCADE через ForeignKey))
def delete_director(db: Session, director_id: int):
    db_director = get_director(db, director_id)
    if db_director:
        db.delete(db_director)
        db.commit()
        return True
    return False