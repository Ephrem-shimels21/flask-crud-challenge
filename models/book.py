from datetime import date
from uuid import uuid4


class Book:
    def __init__(self, title, author, price, category, publication_year):
        if not isinstance(publication_year, date):
            raise ValueError("Publication year must be a valid date")

        self.id = str(uuid4())
        self.title = title
        self.author = author
        self.price = price
        self.category = category
        self.publication_year = publication_year

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title if self.title is not None else "",
            "author": self.author if self.author is not None else "",
            "price": self.price if self.price is not None else 0,
            "category": self.category if self.category is not None else [],
            "publication_year": (
                self.publication_year if self.publication_year is not None else ""
            ),
        }
