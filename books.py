## data class
# only job of a data class is to aggregate data
# Authors: Oleg, Liam, Henry
class Book:

    ## constructor
    def __init__(self, isbn: str, title: str, author: str, year: int, publisher: str):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.publisher = publisher

    ## string representation (toString)
    ## return a human readable string nicely formatted
    def __str__(self):
        return f"{self.isbn}, {self.title}, {self.author}, {self.year}, {self.publisher}"

    ## representation of the object
    def __repr__(self):
        return f"Book({self.isbn}, {self.title}, {self.author}, {self.year}, {self.publisher})"
