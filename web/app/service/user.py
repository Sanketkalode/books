from app.models.user import User


def get_user(username):
    user = User.objects(username=username).first()
    return user


def check_username_password(username, password):
    user = get_user(username)

    if user:
        if user.password == password:
            return True
    return False
