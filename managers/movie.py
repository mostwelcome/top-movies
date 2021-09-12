from database.models.tables.movie import Movie
import json
from helpers.exceptions.movie_exception import MovieError


def add_movie_details(movie):
    try:
        return Movie.create(title=movie.title, description=movie.description, rating=movie.rating, ranking=movie.ranking,
                            review=movie.review)
    except Exception:
        return MovieError(error_code=500, error_message='Internal Server Error', error_details='Error while adding movie details')


def get_movies_list():
    try:
        movies = Movie.get_all_movies()
        return movies
    except Exception as e:
        return MovieError(error_code=500, error_message='Internal Server Error', error_details='Error while getting movie details')


def update_movie(id, movie):
    try:
        old_movie_obj = Movie.get_movie(id)
        if not old_movie_obj:
            raise MovieError(
                error_code=404, error_message='movie id not found')
        setattr(old_movie_obj, 'rating', movie.rating)
        return old_movie_obj.save()
    except MovieError as err:
        return err
    except Exception:
        return MovieError(error_code=500, error_message='Internal Server Error', error_details='Error while updating movie details')


def delete_movie_details(id):
    try:
        movie = Movie.get_movie(id)
        if not movie:
            raise MovieError(
                error_code=404, error_message='movie id not found')
        return Movie.delete_movie(movie)
    except MovieError as err:
        return err
    except Exception:
        return MovieError(error_code=500, error_message='Internal Server Error', error_details='Error while deleting movie details')
