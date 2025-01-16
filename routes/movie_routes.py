from fastapi import FastAPI, HTTPException
from models.movie_models import MovieIn, MovieOut
from controllers.movie_controller import (
    create_movie,
    read_movies,
    read_movie_by_id,
    update_movie_by_id,
    delete_movie_by_id,
)

app = FastAPI()


@app.get("/movies", response_model=list[MovieOut], status_code=200)
def get_all_movies():
    """Retrieves all movies from the database.

    Returns:
        list: List of all movies in the database.
    """
    return read_movies()


@app.get("/movies/{movie_id}", response_model=list[MovieOut], status_code=200)
def get_movie_by_id(movie_id: int):
    """Retrieves a specific movie by its ID.

    Args:
        movie_id (int): ID of the movie to retrieve.

    Raises:
        HTTPException: If the movie is not found.

    Returns:
        list: List with the movie data.
    """
    result = read_movie_by_id(movie_id)

    if not result:
        raise HTTPException(status_code=404, detail="Movie not found")

    return result


@app.post("/movies", status_code=201)
def add_movie(new_movie: MovieIn):
    """Adds a new movie to the database.

    Args:
        new_movie (MovieIn): Movie data to insert.

    Returns:
        dict: Success message.
    """
    create_movie(new_movie)

    return {"message": "Movie added successfully"}


@app.put("/movies/{movie_id}", status_code=200)
def update_movie_by_id(movie_id: int, new_movie: MovieIn):
    """Updates a movie by its ID.

    Args:
        movie_id (int): ID of the movie to update.
        new_movie (MovieIn): New data for the movie.

    Raises:
        HTTPException: If the movie is not found.

    Returns:
        dict: Success message.
    """
    if not get_movie_by_id(movie_id):
        raise HTTPException(status_code=404, detail="Movie not found")

    update_movie_by_id(movie_id, new_movie)
    return {"message": "Movie updated successfully"}


@app.delete("/movies/{movie_id}", status_code=200)
def del_movie_by_id(movie_id: int):
    """Deletes a movie by its ID.

    Args:
        movie_id (int): ID of the movie to delete.

    Raises:
        HTTPException: If the movie is not found.

    Returns:
        dict: Success message.
    """
    if not get_movie_by_id(movie_id):
        raise HTTPException(status_code=404, detail="Movie not found")

    delete_movie_by_id(movie_id)

    return {"message": "Movie deleted successfully"}
