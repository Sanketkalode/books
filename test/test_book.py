import datetime
import json
from unittest import TestCase

from mongoengine import get_db, disconnect

import app
from app import create_app
from app.models.books import Book
from config.testing import TestingConfig


class TestBook(TestCase):
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

    def test_book(self):
        book = Book(bookID=1, title='How to Kill a Mocking bird',
                    authors='NewAuthor', average_rating=3.75, isbn='safasfd', isbn13=1234567, language_code='EN',
                    num_pages=34, ratings_count=1232, text_reviews_count=23, publication_date=datetime.datetime.now(),
                    publisher='Sanket', description='Test', url="https://www.goodreads.com/book/show/1"
                                                                ".Harry_Potter_and_the_Half-Blood_Prince",
                    coverImage="https://www.goodreads.com/book/show/1.Harry_Potter_and_the_Half-Blood_Prince")
        book.save()
        new_book = Book.objects(title='How to Kill a Mocking bird').first()
        self.assertEqual(new_book.authors, 'NewAuthor')

    def test_book_route(self):
        book_dict = {"bookID": "1",
                     "title": "Harry Potter and the Half-Blood Prince (Harry Potter  #6)", "authors": "J.K. Rowling",
                     "average_rating": 4.57, "isbn": "0439785960", "isbn13": "9780439785969",
                     "language_code": "eng", "num_pages": 652, "ratings_count": "2095690",
                     "text_reviews_count": "27591",
                     "publication_date": "2006-09-16", "publisher": "Scholastic Inc.",
                     "description": "The war against Voldemort is not going well; even Muggle governments are "
                                    "noticing. Ron scans the obituary pages of the Daily Prophet, looking for "
                                    "familiar names. Dumbledore is absent from Hogwarts for long stretches of time, "
                                    "and the Order of the Phoenix has already suffered losses.And yet . . .As in all "
                                    "wars, life goes on. The Weasley twins expand their business. Sixth-year students "
                                    "learn to Apparate - and lose a few eyebrows in the process. Teenagers flirt and "
                                    "fight and fall in love. Classes are never straightforward, through Harry "
                                    "receives some extraordinary help from the mysterious Half-Blood Prince.So it's "
                                    "the home front that takes center stage in the multilayered sixth installment of "
                                    "the story of Harry Potter. Here at Hogwarts, Harry will search for the full and "
                                    "complete story of the boy who became Lord Voldemort - and thereby find what may "
                                    "be his only vulnerability.",
                     "url": "https://www.goodreads.com/book/show/1.Harry_Potter_and_the_Half-Blood_Prince",
                     "coverImage": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1587697303l"
                                   "/1._SX318_.jpg",
                     "genre": ["Fantasy", "Young Adult", "Fiction", "Fantasy", "Childrens", "Adventure", "Audiobook",
                               "Childrens", "Classics", "Science Fiction Fantasy"],
                     "other_editions": ["Harry Potter and the Half-Blood Prince (Harry Potter #6)",
                                        "Harry Potter and the Half-Blood Prince (Harry Potter, #6)",
                                        "Harry Potter and the Half-Blood Prince (Harry Potter, #6)",
                                        "Harry Potter and the Half-Blood Prince (Harry Potter, #6)",
                                        "Harry Potter and the Half-Blood Prince (Harry Potter, #6)"],
                     "other_editions_covers": [
                         "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1449583624i/28139880"
                         "._UY200_.jpg",
                         "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1567294600i/49852"
                         "._UY200_.jpg",
                         "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1361297007i/93124"
                         "._UY200_.jpg",
                         "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1453889268i/28767931"
                         "._UY200_.jpg",
                         "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1406762177i/22844202"
                         "._UY200_.jpg"],
                     "series_list": ["Harry Potter and the Sorcerer's Stone (Harry Potter, #1)",
                                     "Harry Potter and the Chamber of Secrets (Harry Potter, #2)",
                                     "Harry Potter and the Prisoner of Azkaban (Harry Potter, #3)",
                                     "Harry Potter and the Goblet of Fire (Harry Potter, #4)",
                                     "Harry Potter and the Order of the Phoenix (Harry Potter, #5)",
                                     "Harry Potter and the Deathly Hallows (Harry Potter, #7)"],
                     "series_list_cover": [
                         "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1474154022l/3._SY75_"
                         ".jpg",
                         "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1474169725l/15881"
                         "._SY75_.jpg",
                         "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1630547330l/5._SY75_"
                         ".jpg",
                         "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1554006152l/6._SX50_"
                         ".jpg",
                         "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1546910265l/2._SX50_"
                         ".jpg",
                         "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1474171184l/136251"
                         "._SY75_.jpg"]}

        book = Book(**book_dict)
        book.save()
        data = json.dumps({
            'id': 1
        })
        with self.app.test_client() as c:
            response = c.get('/book/', headers={"Content-Type": "application/json"}, data=data)
            self.assertEqual(response.json['Title'], "Harry Potter and the Half-Blood Prince (Harry Potter  #6)")
            self.assertEqual(response.status_code, 200)
