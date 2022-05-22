import os


class DevelopmentConfig(object):
    """Development Config"""
    DEBUG = True
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY") or 'sanket'
    MONGODB_SETTINGS = {
        'db': 'BooksDB',
        'host': 'localhost',
        'port': 27017
    }
