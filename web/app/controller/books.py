from app.service.books import getBook
from flask import Blueprint, request, jsonify

book_blueprint = Blueprint("book", __name__, url_prefix="/book")


@book_blueprint.route('/', methods=["GET"])
def get_book():
    data = request.get_json()
    id = data["id"]
    book = getBook(id)
    return jsonify(book)
