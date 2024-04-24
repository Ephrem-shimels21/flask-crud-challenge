from models.book import Book


class BookStorage:
    def __init__(self):
        self.books = []

    def get_books(self):
        return [book.to_dict() for book in self.books]

    def get_book_by_id(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book.to_dict()
        return None

    def add_book(self, title, author, price, category, publication_year):
        new_book = Book(title, author, price, category, publication_year)
        self.books.append(new_book)
        return new_book.to_dict()

    def update_book(self, book_id, updated_book):
        book = next((book for book in self.books if book.id == book_id), None)
        if book:
            book.title = updated_book.get("title", book.title)
            book.author = updated_book.get("author", book.author)
            book.price = updated_book.get("price", book.price)
            book.category = updated_book.get("category", book.category)
            book.publication_year = updated_book.get(
                "publication_year", book.publication_year
            )
            return book.to_dict()
        return None

    def delete_book(self, book_id):
        book = next((book for book in self.books if book.id == book_id), None)
        if book:
            self.books.remove(book)
            return True
        return False
