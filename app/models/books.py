import mongoengine as me


class Book(me.Document):
    id = me.SequenceField(primary_key=True)
    bookID = me.LongField(required=True, unique=True)
    title = me.StringField(required=True)
    authors = me.StringField(required=True)
    average_rating = me.FloatField(required=True, max_value=5)
    isbn = me.StringField(required=True, unique=True, max_length=13)
    isbn13 = me.LongField(required=True, unique=True, max_length=13)
    language_code = me.StringField(required=True)
    num_pages = me.IntField(required=True)
    ratings_count = me.LongField(required=True)
    text_reviews_count = me.LongField(required=True)
    publication_date = me.DateTimeField(required=True)
    publisher = me.StringField(required=True)
    description = me.StringField(required=True)
    url = me.URLField(required=True)
    coverImage = me.URLField(required=True)
    genre = me.ListField(null=[])
    other_editions = me.ListField(null=[])
    other_editions_covers = me.ListField(me.URLField(), null=[])
    series_list = me.ListField(null=[])
    series_list_cover = me.ListField(me.URLField(), null=[])

    def to_json(self):
        return {
            'Title': self.title,
            'Author': self.authors,
            'Rating': self.average_rating,
            'ISBN': self.isbn,
            'Publisher': self.publisher,
            'Date of Publication': self.publication_date,
            'Description': self.description,
            'Cover': self.coverImage,
            'Series': self.series_list
        }
