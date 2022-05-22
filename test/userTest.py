import os
import unittest

from mongoengine import get_db, disconnect

import app
from app import create_app
from app.models.user import User
from config.testing import TestingConfig


class TestUserModel(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestingConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        db = get_db()
        for collection in db.list_collection_names():
            db.drop_collection(collection)
        disconnect(app.db)
        self.app_context.pop()

    def test_test_config(self):
        self.assertTrue(self.app.config['SECRET_KEY'], "sanket")
        self.assertTrue(self.app.config['TESTING'])

    def test_encode_auth_token(self):
        user = User(username='test', password='test123')
        user.save()
        print(os.environ.get('SECRET_KEY'))
        auth_token = user.encode_auth_token(user.username)
        print(auth_token)
        self.assertTrue(isinstance(auth_token, bytes))


if __name__ == '__name__':
    unittest.main(verbosity=3)
