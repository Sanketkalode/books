from app.service.user import check_username_password
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

user_blueprint = Blueprint("user", __name__)


@user_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    if check_username_password(username, password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Bad username or password"}), 401


@user_blueprint.route('/user', methods=['GET'])
@jwt_required()
def user():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
