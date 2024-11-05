from queryFunctions import avg_rating_top_ten
from queryFunctions import top_authors
from queryFunctions import top_books_by_ratings
from tabulate import tabulate
from connect import connect





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