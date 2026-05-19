# Movie API - FastAPI

A REST API for managing movies and directors built with FastAPI and SQLAlchemy.

## Quick Start

```bash
# Install dependencies
pip install fastapi uvicorn sqlalchemy

# Run server
uvicorn main:app --reload
```

API available at `http://127.0.0.1:8000/docs`

## Project Structure

- `main.py` - API routes
- `models.py` - Database models (Movie, Director)
- `schemas.py` - Data validation (Pydantic)
- `crud.py` - Database operations
- `database.py` - Database configuration

## Key Endpoints

### Directors
- `GET /directors` - List all directors
- `GET /directors/{id}` - Get director with their movies
- `POST /directors` - Create director
- `PUT /directors/{id}` - Update director
- `DELETE /directors/{id}` - Delete director (cascades to movies)

### Movies
- `GET /movies` - List all movies
- `GET /movies/{id}` - Get specific movie
- `POST /movies` - Create movie
- `PUT /movies/{id}` - Update movie
- `DELETE /movies/{id}` - Delete movie

## Database

SQLite database with two tables:
- **directors** - id, name, country, created_at
- **movies** - id, title, year, genre, rating, director_id, created_at

Movies are linked to directors via foreign key. When a director is deleted, their movies are deleted automatically (CASCADE).

## Data Validation

- Movie title: non-empty string
- Year: 1900-2100
- Rating: 0.0-10.0
- Director name & country: non-empty strings

Invalid data returns `422 Unprocessable Entity`.

## Testing with Swagger UI

FastAPI provides interactive API documentation at `/docs`:

```
http://127.0.0.1:8000/docs
```

You can test all endpoints directly in the browser:
1. Click on an endpoint
2. Click "Try it out"
3. Enter request data (JSON)
4. Click "Execute"
5. View the response

This is the easiest way to test the API during development.

## HTTP Status Codes

- `200` - OK
- `201` - Created
- `204` - No Content (deleted)
- `404` - Not Found
- `422` - Validation Error

## Example

```bash
# Create director
curl -X POST "http://127.0.0.1:8000/directors" \
  -H "Content-Type: application/json" \
  -d '{"name": "Christopher Nolan", "country": "UK"}'

# Create movie
curl -X POST "http://127.0.0.1:8000/movies" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Inception",
    "year": 2010,
    "genre": "Sci-Fi",
    "rating": 8.8,
    "director_id": 1
  }'

# Get director with movies
curl "http://127.0.0.1:8000/directors/1"
```

## Technologies

- FastAPI - Web framework
- SQLAlchemy - ORM
- Pydantic - Data validation
- SQLite - Database
- Uvicorn - ASGI server
