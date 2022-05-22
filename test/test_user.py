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

    def test_function(self):
        self.assertEqual(0, 0)

    def test_user(self):
        user = User(username='Sanket', password='1234')
        user.save()

        new_user = User.objects(username='Sanket').first()
        self.assertEqual(new_user.username, user.username)


if __name__ == '__name__':
    unittest.main(verbosity=3)
