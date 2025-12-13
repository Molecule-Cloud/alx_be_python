class Book:
    def __init__(self, author, title):
        self.title = title
        self.author = author


class EBook(Book):
    def __init__(self, author, title, file_size):
        super().__init__(author, title)
        self.file_size = file_size

    
class PrintBook(Book):
    def __init__(self, author, title, page_count):
        super().__init__(author, title)
        self.page_count = page_count

class Library:
    def __init__(self, books=None):
        if books is None:
            books = []
        self.books = books

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author}")

