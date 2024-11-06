# Authors: Oleg, Liam, Henry

from tabulate import tabulate
import ratings_queries
import unittest
from connect import connect
from ratings_queries import avg_rating_top_ten
from ratings import Ratings


class TestRatings(unittest.TestCase):
    def test_avg_rating_top_ten(self):
        conn = connect()
        header = ["ID", "Number of Ratings", "Average Rating"]
        x = tabulate(avg_rating_top_ten(conn), headers = header, tablefmt="psql")
        with open("gold/avg_rating_top_ten_output.txt", "r") as f:
            self.assertEqual(x, f.read())
        conn.close()

    def test_insert_rating(self):
        conn = connect()
        prating = Ratings("123", "100", "5") # Rating that will be added to ratings table; does not exist yet
        nrating = Ratings("274308", "0449205983", "0") # Rating exists in rating table
        assert ratings_queries.insert_rating(conn, prating) == True # Insertion of rating should pass; True
        assert ratings_queries.insert_rating(conn, nrating) == False #Insertion of rating already in rating table should fail; False
        conn.close()


