# Authors: Oleg, Liam, Henry

from psycopg import Connection
from typing import List, Tuple
from ratings import Ratings


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


def insert_rating(conn: Connection, rating: Ratings) -> None:
    """
    Insert a rating into rating table
    :param conn: Connection - a database connection
    :param title: book, book data i.e isbn, author, year, publisher
    :return: None
    """

    query = """
    INSERT INTO ratings (User_id, ISBN, ratings)
    VALUES (%s, %s, %s)
    """

    # Using parameterized queries to avoid SQL injection
    conn.execute(query, (rating.User_id, rating.ISBN, rating.ratings))
    conn.commit()  # Commit the transaction
