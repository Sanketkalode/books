from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_mongoengine import MongoEngine

db = MongoEngine()
jwt = JWTManager()


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    add_extensions(app)
    add_blueprints(app)

    return app


def add_extensions(app):
    db.init_app(app)
    jwt.init_app(app)
    CORS(app, resource={r"/": {"origins": "*"}})


def add_blueprints(app):
    from app.controller import views
    app.register_blueprint(views)
    from app.controller.author import auth_blueprint
    app.register_blueprint(auth_blueprint)
    from app.controller.books import book_blueprint
    app.register_blueprint(book_blueprint)
