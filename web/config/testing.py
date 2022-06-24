import datetime
import os


class TestingConfig(object):
    """Testing Config"""
    DEBUG = True
    TESTING = True
    SECRET_KEY = os.environ.get("SECRET_KEY") or 'sanket'
    MONGODB_SETTINGS = {
        'db': 'TestBooksDB',
        'host': 'localhost',
        'port': 27017
    }
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=5)