from database.models.tables.movie import Movie
import json
from flask import jsonify


def add_movie_details(movie):
    return jsonify(Movie.create(title=movie.title, description=movie.description, rating=movie.rating, ranking=movie.ranking,
                                review=movie.review))


def get_movies_list():
    movies = Movie.get_all_movies()
    print(movies)
    print(type(movies))
    for movie in movies:
        print(movie.id, movie.title)
    return jsonify(movies)


def update_movie_info():
    pass


def delete_movie():
    pass
