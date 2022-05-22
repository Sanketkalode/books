from app.models.books import Book


def getBook(id):
    book = Book.objects(id=id).first()
    if book:
        return book.to_json()
    else:
        return {
            "message": "Book not Found"
        }
