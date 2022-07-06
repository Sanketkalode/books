import unittest
from unittest import TestCase

from mongoengine import disconnect
from mongoengine import get_db

from web import app
from web.app import create_app, db
from web.config.testing import TestingConfig


class TestApp(TestCase):
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

    def test_db(self):
        self.assertEqual(db.get_db().name, "TestBooksDB")

    def test_home_route(self):
        with self.app.test_client() as c:
            response = c.get('/', headers={"Content-Type": "application/json"})
            self.assertEqual(response.json['message'], "Welcome to book.com v.2")

    def test_appConfig(self):
        self.assertEqual(self.app.config['SECRET_KEY'], 'sanket')
        self.assertTrue(self.app.config['TESTING'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
