import datetime
import os


class ProductionConfig(object):
    """Production Config"""
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY") or 'sanket'
    MONGODB_SETTINGS = {
        'db': os.environ.get("MONGODB_DATABASE") or 'BooksDB',
        'host': os.environ.get("MONGODB_HOSTNAME") or 'localhost',
        'port': int(os.environ.get("MONGODB_PORT")) or 27017
    }
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=15)
