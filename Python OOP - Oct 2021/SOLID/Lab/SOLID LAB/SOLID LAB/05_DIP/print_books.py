class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    def format(self, book: Book):
        return book.content


class Printer(Formatter):
    def get_book(self, book: Book):
        return self.get_book(book)