# Authors: Oleg, Liam, Henry

from psycopg import Connection
from typing import List, Tuple
from users import Users


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
    conn.commit()
