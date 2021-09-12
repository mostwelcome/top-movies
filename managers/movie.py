from database.models.tables.movie import Movie
import json
from flask import jsonify


def add_movie_details(movie):
    return jsonify(Movie.create(title=movie.title, description=movie.description, rating=movie.rating, ranking=movie.ranking,
                                review=movie.review))


def get_movies_list():
    movies = Movie.get_all_movies()
    return jsonify(movies)


def update_movie(id, movie):
    old_movie_obj = Movie.get_movie(id)
    old_movie_obj.rating = movie.rating
    old_movie_obj.save()


def delete_movie_details(id):
    movie = Movie.get_movie(id)
    return Movie.delete_movie(movie)
