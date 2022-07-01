from flask import Blueprint, jsonify

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return jsonify({
        'message': "Welcome to book.com v.2"
    }), 200
