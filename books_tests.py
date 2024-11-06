# Authors: Oleg, Liam, Henry

import unittest
from tabulate import tabulate
import books_queries
from connect import connect
from books_queries import top_authors
from books import Book



class booksTests(unittest.TestCase):
    #unit test to see if the output of top_authors is equal to top_authors_output.txt in gold folder
    def test_top_authors(self):
        conn = connect()
        header = ["Author", "Number of Books"]
        x = tabulate(top_authors(conn, 5), headers = header, tablefmt= "psql")
        with open("gold/top_authors_output.txt", "r") as f:
            self.assertEqual(x, f.read())
        conn.close()



    def test_top_books_by_ratings(self):
        conn = connect()
        header = ["Title", "Author", "num_rating"]
        x = tabulate(books_queries.top_books_by_ratings(conn, 5), headers = header, tablefmt= "psql")
        with open("gold/top_books_by_rating_output.txt", "r") as f:
            self.assertEqual(x, f.read())
        conn.close()

    def test_insert_book(self):
        conn = connect()
        nbook = Book("0195153448", "Classical Mythology", "Mark P. O. Morford", 2002, "Oxford Univeristy Press")
        pbook = Book("100", "Harry Potter", "J.K Rowling", 1999, "British Publisher")
        assert book_queries.insert_book(conn, pbook) == True
        assert book_queries.insert_book(conn, nbook) == False
        
