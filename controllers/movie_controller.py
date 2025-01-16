from sqlmodel import SQLModel, Session, select
from ex6.models.movie_models import MovieIn, MovieOut
from ex6.models.database import engine


def convert_results(results):
    results_arr = []

    for row in results:
        inner_dict = {
            "id": row.id,
            "title": row.title,
            "director": row.director,
            "category": row.category,
            "year": row.year,
        }
        results_arr.append(inner_dict)

    return results_arr


def create_movie(new_movie: MovieOut):
    with Session(engine) as session:
        session.add(new_movie)
        session.commit()


def read_movies():
    with Session(engine) as session:
        statement = select(MovieOut)
        results = session.exec(statement)
        return convert_results(results)


def read_movie_by_id(id: int):
    with Session(engine) as session:
        statement = select(MovieOut).where(MovieOut.id == id)
        results = session.exec(statement)

        return convert_results(results)


def update_movie_by_id(id: int, new_movie: MovieOut):
    with Session(engine) as session:
        if not read_movie_by_id(id):
            return

        statement = select(MovieOut).where(MovieOut.id == id)
        results = session.exec(statement)

        movie = results.one()

        movie.title = new_movie.title
        movie.director = new_movie.director
        movie.category = new_movie.category
        movie.year = new_movie.year

        session.add(movie)
        session.commit()


def delete_movie_by_id(id):
    with Session(engine) as session:
        if not read_movie_by_id(id):
            return

        statement = select(MovieOut).where(MovieOut.id == id)
        results = session.exec(statement)

        movie = results.one()

        session.delete(movie)
        session.commit()
