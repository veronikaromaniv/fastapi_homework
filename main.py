from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import models, schemas, crud
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Movie API", version="1.0")


# MOVIE ENDPOINTS

@app.get("/movies", response_model=List[schemas.MovieResponse])
def read_movies(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_movies(db, skip=skip, limit=limit)


@app.get("/movies/{movie_id}", response_model=schemas.MovieResponse)
def read_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = crud.get_movie(db, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Фільм не знайдено")
    return movie


@app.post("/movies", response_model=schemas.MovieResponse, status_code=201)
def create_movie(movie: schemas.MovieCreate, db: Session = Depends(get_db)):
    return crud.create_movie(db, movie)


@app.put("/movies/{movie_id}", response_model=schemas.MovieResponse)
def update_movie(movie_id: int, movie: schemas.MovieCreate, db: Session = Depends(get_db)):
    updated = crud.update_movie(db, movie_id, movie)
    if not updated:
        raise HTTPException(status_code=404, detail="Фільм не знайдено")
    return updated


@app.delete("/movies/{movie_id}", status_code=204)
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    if not crud.delete_movie(db, movie_id):
        raise HTTPException(status_code=404, detail="Фільм не знайдено")
    return None


# DIRECTOR ENDPOINTS

@app.get("/directors", response_model=List[schemas.DirectorResponse])
def read_directors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_directors(db, skip=skip, limit=limit)


@app.get("/directors/{director_id}", response_model=schemas.DirectorResponse)
def read_director(director_id: int, db: Session = Depends(get_db)):
    director = crud.get_director(db, director_id)
    if not director:
        raise HTTPException(status_code=404, detail="Режисер не знайдено")
    return director


@app.post("/directors", response_model=schemas.DirectorResponse, status_code=201)
def create_director(director: schemas.DirectorCreate, db: Session = Depends(get_db)):
    return crud.create_director(db, director)


@app.put("/directors/{director_id}", response_model=schemas.DirectorResponse)
def update_director(director_id: int, director: schemas.DirectorCreate, db: Session = Depends(get_db)):
    updated = crud.update_director(db, director_id, director)
    if not updated:
        raise HTTPException(status_code=404, detail="Режисер не знайдено")
    return updated


@app.delete("/directors/{director_id}", status_code=204)
def delete_director(director_id: int, db: Session = Depends(get_db)):
    if not crud.delete_director(db, director_id):
        raise HTTPException(status_code=404, detail="Режисер не знайдено")
    return None


@app.get("/directors/{director_id}/movies", response_model=List[schemas.MovieResponse])
def read_director_movies(director_id: int, db: Session = Depends(get_db)):
    director = crud.get_director(db, director_id)
    if not director:
        raise HTTPException(status_code=404, detail="Режисер не знайдено")
    return director.movies