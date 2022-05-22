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


@jwt.user_identity_loader
def user_idenity_lookup(user):
    return user.id


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.objects(id=identity).first()
