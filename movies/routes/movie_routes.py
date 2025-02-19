from fastapi import APIRouter, Depends
from movies.models.movie_models import MovieIn, MovieOut
from sqlmodel import Session
from movies.db.session import get_session
from movies.controllers.movie_controller import (
    create_movie,
    read_movies,
    read_movie_by_id,
    update_movie_by_id,
    delete_movie_by_id,
)

router = APIRouter()


@router.get("/movies", response_model=list[MovieOut], status_code=200)
def get_all_movies(session: Session = Depends(get_session)):
    """Retrieves all movies from the database.

    Returns:
        list: List of all movies in the database.
    """
    return read_movies(session)


@router.get("/movies/{movie_id}", response_model=MovieOut, status_code=200)
def get_movie_by_id(movie_id: int, session: Session = Depends(get_session)):
    """Retrieves a specific movie by its ID.

    Args:
        movie_id (int): ID of the movie to retrieve.

    Raises:
        HTTPException: If the movie is not found.

    Returns:
        dict: movie data.
    """
    result = read_movie_by_id(session, movie_id)

    return result


@router.post("/movies", status_code=201)
def add_movie(new_movie: MovieIn, session: Session = Depends(get_session)):
    """Adds a new movie to the database.

    Args:
        new_movie (MovieIn): Movie data to insert.

    Returns:
        dict: Success message.
    """
    create_movie(session, new_movie)

    return {"message": "Movie added successfully"}


@router.put("/movies/{movie_id}", status_code=200)
def update_movie(movie_id: int, new_movie: MovieIn, session: Session = Depends(get_session)):
    """Updates a movie by its ID.

    Args:
        movie_id (int): ID of the movie to update.
        new_movie (MovieIn): New data for the movie.

    Raises:
        HTTPException: If the movie is not found.

    Returns:
        dict: Success message.
    """
    update_movie_by_id(session, movie_id, new_movie)
    return {"message": "Movie updated successfully"}


@router.delete("/movies/{movie_id}", status_code=200)
def del_movie_by_id(movie_id: int, session: Session = Depends(get_session)):
    """Deletes a movie by its ID.

    Args:
        movie_id (int): ID of the movie to delete.

    Raises:
        HTTPException: If the movie is not found.

    Returns:
        dict: Success message.
    """
    delete_movie_by_id(session, movie_id)

    return {"message": "Movie deleted successfully"}
