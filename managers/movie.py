from database.models.tables.movie import Movie
import json

def add_movie():
    pass

def get_movies_list():
    movies = Movie.get_all_movies()
    return json.dumps(movies)

def update_movie_info():
    pass

def delete_movie():
    pass