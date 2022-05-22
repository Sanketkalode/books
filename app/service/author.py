from app.models.author import Author
from app.service.books import getBook


def getAuthorName(id):
    auth = Author.objects(id=id).first()
    if auth:
        return auth.to_json()
    else:
        return {'Message': "Author not Found"}


def getBooksName(id):
    auth = Author.objects(id=id).first()
    if not auth:
        return {'Message': "Author not Found"}
    else:
        book_list = []
        for b in auth.books:
            book = getBook(b)
            book_list.append(book)
        return book_list

