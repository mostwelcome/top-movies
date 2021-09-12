from database.models.tables.movie import Movie
from flask import Blueprint, request
from managers.movie import add_movie_details, delete_movie_details, get_movies_list, update_movie
from flask import jsonify


MOVIES_BOOKPRINT = Blueprint('movies', __name__)


@MOVIES_BOOKPRINT.route('', methods=['GET'])
def movies_list():
    return jsonify(get_movies_list())


@MOVIES_BOOKPRINT.route('', methods=['POST'])
def add_movie():
    obj = Movie(**request.get_json())
    return jsonify(add_movie_details(obj))


@MOVIES_BOOKPRINT.route('/<id>', methods=['PUT'])
def update_movie_info(id=None):
    obj = Movie(**request.get_json())
    return jsonify(update_movie(id,obj))


@MOVIES_BOOKPRINT.route('/<id>', methods=['DELETE'])
def delete_movie(id=None):
    return jsonify(delete_movie_details(id))
     
