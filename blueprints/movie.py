from database.models.tables.movie import Movie
from flask import Blueprint, request
from managers.movie import get_movies_list


MOVIES_BOOKPRINT = Blueprint('movies', __name__)


@MOVIES_BOOKPRINT.route('', methods=['GET'])
def movies_list():
    return get_movies_list()


@MOVIES_BOOKPRINT.route('', methods=['POST'])
def add_movie():
    print(request.get_json())
    return {'method': 'POST'}


@MOVIES_BOOKPRINT.route('', methods=['PUT'])
def update_movie_info():
    return {'method': 'PUT'}


@MOVIES_BOOKPRINT.route('', methods=['DELETE'])
def delete_movie():
    return {'method': 'DELETE'}
