# Authors: Oleg, Liam, Henry

from book import Book
from book_queries import insert_book
from ratings import Ratings
from ratings_queries import insert_rating
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

    header = ["ID", "Number of Ratings", "Average Rating"]
    print(tabulate(avg_rating_top_ten(conn), headers= header , tablefmt= "psql"))
    conn.close()


if __name__ == "__main__":
    conn = connect()

    header = ["Author", "Number of Books"]
    print(tabulate(top_authors(conn, 5),headers = header, tablefmt= "psql"))
    conn.close()



if __name__ == "__main__":
    conn = connect()

    header = ["Title", "Author", "num_rating"]
    print(tabulate(top_books_by_ratings(conn, 5), headers = header,tablefmt= "psql"))
    conn.close()

if __name__ == "__main__":
    conn = connect()
    print("INFO: Got a connection")
    pbook = Book("100", "Harry Potter", "J.K Rowling", 1999, "British Publisher")
    print(insert_book(conn, pbook))
    conn.close()

if __name__ == "__main__":
    conn = connect()
    print("INFO: Got a connection")
    prating = Ratings("123", "100", "5")    
    print(insert_rating(conn, prating))
    conn.close()
