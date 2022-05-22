import mongoengine as me

from app import jwt


class User(me.Document):
    id = me.SequenceField(primary_key=True)
    username = me.StringField(required=True)
    password = me.StringField(required=True)

    def check_password(self, password):
        if self.password == password:
            return True
        return False
