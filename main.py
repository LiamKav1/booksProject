from ratings_queries import avg_rating_top_ten
from books_queries import top_authors
from books_queries import top_books_by_ratings
from books_queries import books_avg_rating
from books_queries import author_avg_book_rating
from users_queries import insert_user
from tabulate import tabulate
from connect import connect


if __name__ == "__main__":
    conn = connect()
    print("INFO: Got a connection")

    print(author_avg_book_rating(conn, "A.A. Milne"))
    conn.close()


if __name__ == "__main__":
    conn = connect()
    print("INFO: Got a connection")

    print(books_avg_rating(conn, "John Steinbeck", "Of Mice and Men"))
    conn.close()


if __name__ == "__main__":
    conn = connect()
    print("INFO: Got a connection")

    print(tabulate(avg_rating_top_ten(conn), tablefmt= "psql"))
    conn.close()


if __name__ == "__main__":
    conn = connect()
    print("INFO: Got a connection")

    print(tabulate(top_authors(conn, 5), tablefmt= "psql"))
    conn.close()



if __name__ == "__main__":
    conn = connect()
    print("INFO: Got a connection")

    print(tabulate(top_books_by_ratings(conn, 5), tablefmt= "psql"))
    conn.close()