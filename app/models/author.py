import mongoengine as me


class Author(me.Document):
    id = me.SequenceField(primary_key=True)
    name = me.StringField(required=True, unique=True)
    books = me.ListField(null=[])

    def to_json(self):
        return {
            'name': self.name
        }
