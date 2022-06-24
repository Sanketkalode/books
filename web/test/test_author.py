import json
from unittest import TestCase

from mongoengine import get_db, disconnect

from web import app
from web.app import create_app
from web.app.models.author import Author
from web.config.testing import TestingConfig


class TestAuthor(TestCase):
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

    def test_Author(self):
        auth = Author(name='Sanket')
        auth.save()

        new_auth = Author.objects().first()

        self.assertEqual(new_auth.name, "Sanket")

    def test_auth_route(self):
        data = json.dumps({
            'id': 1
        })
        auth = Author(name='Sanket', books=[1, 2, 3, 4, 5])
        auth.save()
        with self.app.test_client() as c:
            response = c.get('/author/', headers={"Content-Type": "application/json"}, data=data)
            self.assertEqual(response.json['name'], "Sanket")
            self.assertEqual(response.status_code, 200)
