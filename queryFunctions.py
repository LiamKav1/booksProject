from psycopg import Connection
from typing import List, Tuple
from ratings import Ratings
from users import Users
from books import Book


def format_author_for_query(author_name):
    # Remove dots and spaces, then convert to lowercase
    normalized_author = author_name.replace(" ", "").replace(".", "").lower()
    return normalized_author


    query1 = """
        SELECT 
            AVG(CAST(rating AS INTEGER)) AS Avg_Rating,
            COUNT(isbn) AS num_books
        FROM books
        NATURAL JOIN ratings
        WHERE LOWER(REPLACE(REPLACE(author, ' ', ''), '.', '')) = %s
        GROUP BY LOWER(REPLACE(REPLACE(author, ' ', ''), '.', ''))
        LIMIT %s;
            """
    cur.execute(query1, (format_author_for_query(author), limit))


def format_title_for_query(title_name):
        # Remove dots and spaces, then convert to lowercase
        normalized_title = title_name.replace(" ", "").replace(".", "").lower()
        return normalized_title


    query2 = """ 
    select avg(cast(rating as integer)), COUNT(isbn) AS num_books
    from books natural join ratings
    where LOWER(REPLACE(REPLACE(author, ' ', ''), '.', '')) = %s
    and LOWER(REPLACE(REPLACE(title, ' ', ''), '.', '')) = %s
    limit %s
    """
    cur.execute(query2, (format_author_for_query(author), format_title_for_query(title), limit))



def avg_rating_top_ten(conn: Connection) -> List[Tuple[str, int, float]]:
    """
    Return a list of ratings based on the ISBN.
    :param conn: Connection - a database connection
    :param ISBN: str, the ISBN
    :param limit: int, the number of ratings to return
    :return: a list of ratings
    """


    query = """SELECT 
    user_id AS ID,
    COUNT(rating) AS num_ratings,
    AVG(CAST(rating AS FLOAT)) AS avg_rating
    FROM 
        ratings
    GROUP BY 
        user_id
    ORDER BY 
        num_ratings DESC
    LIMIT 10
        """

    cursor = conn.execute(query)

    rs = []
    for row in cursor:
        rs.append((row[0], row[1], row[2]))

    return rs


def insert_user(conn: Connection, id: str, location: str, age: int):
    """
    Insert a new user into the users table.
    :param conn: Connection - a database connection
    :param user_id: str, the user id
    :param location: str, the location
    :param age: int, the age
    :return: None
    """


    query = """
    INSERT INTO users (id, location, age)
    VALUES (%s, %s, %s)
    """

    conn.execute(query, (id, location, age))


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