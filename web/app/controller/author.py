from app.service.author import getBooksName, getAuthorName
from flask import request, jsonify, Blueprint

auth_blueprint = Blueprint("auth", __name__, url_prefix="/author")


@auth_blueprint.route('/', methods=['GET'])
def get_author():
    data = request.get_json()
    auth = getAuthorName(data['id'])
    return jsonify(auth), 200


@auth_blueprint.route('/books', methods=["GET"])
def get_author_books():
    data = request.get_json()
    books = getBooksName(data['id'])
    return jsonify(books), 200
