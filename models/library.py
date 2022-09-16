from models.book import *

book_1 = Book("The Shipping News", "Annie E Proulx", "Fiction", False, 0)
book_2 = Book("Seven Deaths of Evelyn Hardcastle", "Stuart Turton", "SciFi", False, 1)
book_3 = Book("How Music Works", "David Byrne", "NonFiction", True, 2)
library = [book_1, book_2, book_3]

def add_new_book_to_library(book):
    library.append(book)

def remove_book_from_library(book):
    pass