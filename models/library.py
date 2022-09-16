from models.book import *
import datetime

date_1 = datetime.date(2022, 6, 26)
date_2 = datetime.date(2023, 2, 3)
date_3 = datetime.date(2022, 12, 3)

book_1 = Book("The Shipping News", "Annie E Proulx", "Fiction", False, 0, date_1)
book_2 = Book("Seven Deaths of Evelyn Hardcastle", "Stuart Turton", "SciFi", False, 1, date_2)
book_3 = Book("How Music Works", "David Byrne", "NonFiction", True, 2, date_3)
library = [book_1, book_2, book_3]

def add_new_book_to_library(book):
    library.append(book)

def remove_book_from_library(book):
    pass