from flask import render_template, request
from app import app
from models.library import library, add_new_book_to_library, remove_book_from_library
from models.book import Book


@app.route('/books')
def index():
    return render_template('index.html', title='Home', library=library)

@app.route('/books', methods=['POST'])

def add_book():
    # print(request.form)
    book_title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    checked_out = request.form['checked_out']
    book_id = request.form['book_id']



    if checked_out == "True":
        checked_out_bool = True
    else:
        checked_out_bool = False

    new_book = Book(book_id, book_title, author, genre, checked_out_bool)
    add_new_book_to_library(new_book) # should this be library.add_book_to_library ?

    return render_template('index.html', title='Home', library=library)



@app.route('/book/<book_number>')
def single_order(book_number):
    return render_template('book.html', book=library[int(book_number)]) 


@app.route('/remove/<book_number>')
def remove_book(book_number):
    library.pop(int(book_number))
    return render_template('index.html', title='Home', library=library)
