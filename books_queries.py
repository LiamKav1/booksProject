from psycopg import Connection
from typing import List, Tuple
from books import Book

# queries that operate only on books table

def get_books_by_title(conn: Connection, title: str, limit = 3) -> List[Book]:
    """
    Return a list of books based on the title. By default, only the first 3 books are returned.
    :param conn: Connection - a database connection
    :param title: str, the title of book
    :return: a list of books
    """

    query = """
    SELECT id, author,title, year, publisher 
    FROM books
    WHERE lower(title) = lower(%s)
    ORDER BY year
    LIMIT %s 
    """

    # TODO: check if connection is still live

    cursor = conn.execute(query, (title, limit))

    rs = []
    for row in cursor:
        rs.append(Book(row[0], row[1], row[2], row[3], row[4]))

    return rs




def format_author_for_query(author_name):
    # Remove dots and spaces, then convert to lowercase
    normalized_author = author_name.replace(" ", "").replace(".", "").lower()
    return normalized_author

    # Find an author's average book rating. Output is (Avg Rating, #books). Input is author name.
def author_avg_book_rating(conn: Connection, author: str) -> List[Tuple[float, int]]:
    """
    Return an authors average book rating.
    :param conn: A database connection
    :param author: str, an authors name
    :return: Returns the authors average book rating and the number of books they have published.
    """

    # query = """
    #     SELECT
    #         AVG(CAST(rating AS INTEGER)) AS Avg_Rating,
    #         COUNT(isbn) AS num_books
    #     FROM books
    #     NATURAL JOIN ratings
    #     WHERE LOWER(REPLACE(REPLACE(author, ' ', ''), '.', '')) = %s
    #     GROUP BY LOWER(REPLACE(REPLACE(author, ' ', ''), '.', ''));
    #          """

    query = """
    SELECT AVG(ratings) AS avg_rating, COUNT(*) AS num_books
    FROM books
    WHERE author ~* %s
    """

    cursor = conn.execute(query, (author,))

    rs = []
    for row in cursor:
        rs.append((row[0], row[1]))

    return rs

    def format_title_for_query(title_name):
        # Remove dots and spaces, then convert to lowercase
        normalized_title = title_name.replace(" ", "").replace(".", "").lower()
        return normalized_title


# Find a book's average rating. Input is title and author.
def books_avg_rating(conn: Connection, author: str, title: str) -> Tuple[float, int]:
    """
    Returns the average rating of a book.
    :param conn: A database connection
    :param author: str, The name of the author
    :param title: str, the title of the book
    :return: Return the average rating of the book.
    """

    query = """
    SELECT 
        AVG(CAST(rating AS INTEGER)) AS Avg_Rating,
        COUNT(isbn) AS num_books
    FROM books
    NATURAL JOIN ratings
    WHERE LOWER(REPLACE(REPLACE(author, ' ', ''), '.', '')) = %s
    AND LOWER(REPLACE(REPLACE(title, ' ', ''), '.', '')) = %s
    GROUP BY LOWER(REPLACE(REPLACE(author, ' ', ''), '.', ''));
    """

    cursor = conn.execute(query, (author, title))

    rs = []
    for row in cursor:
        rs.append((row[0], row[1]))

    return rs


def top_authors(conn: Connection, n: int) -> List[Tuple[str, int]]:
    """
    Returns a list of authors and the number of books they have published.
    :param conn: a database connection
    :param n: The number of authors to return
    :return: The list of authros and their total number of published books.
    """

    query = """
    SELECT author, COUNT(title) AS num_books
    FROM books
    GROUP BY author
    ORDER BY num_books DESC
    LIMIT %s
    """

    cursor = conn.execute(query, (n,))

    rs = []
    for row in cursor:
        rs.append((row[0], row[1]))

    return rs



#What are the top n most popular books by number of ratings. Input is n.
# Output is n rows of title, author, number of ratings. What should we order by?
def top_books_by_ratings(conn: Connection, n: int) -> List[Tuple[str, str, int]]:
    """
    Returns a list of the top most popular books by number of ratings.
    :param conn: a database connection
    :param n: The number of books to return
    :return: The list of length n of the most popular books by number of ratings
    """

    query = """
    SELECT title, author, COUNT(rating) AS num_ratings
    FROM books
    JOIN ratings ON books.id = ratings.isbn
    GROUP BY title, author
    ORDER BY num_ratings DESC
    LIMIT %s
    """

    cursor = conn.execute(query, (n,))

    rs = []
    for row in cursor:
        rs.append((row[0], row[1], row[2]))

    return rs


def insert_book(conn: Connection, book: Book) -> None:
    """
    Insert a book into book table
    :param conn: Connection - a database connection
    :param book: book, book data i.e isbn, author, year, publisher
    :return: None
    """

    query = """
    INSERT INTO books (isbn, title, author, year, publisher)
    VALUES (?, ?, ?, ?, ?)
    """

    # Using parameterized queries to avoid SQL injection
    conn.execute(query, (book.isbn, book.title, book.author, book.year, book.publisher))
    conn.commit()












