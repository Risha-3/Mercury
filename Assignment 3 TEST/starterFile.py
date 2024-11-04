# Library Management System

# I have decided to create a list of multiple dictionaries for my library
library = [
    {
        "title": "THE HUNGER GAMES",
        "author": "SUZANNE COLLINS",
        "year": "2008",
        "ISBN": "9780439023481"
    },
    {
        "title": "LORD OF THE FLIES",
        "author": "WILLIAM GOLDING",
        "year": "1954",
        "ISBN": "9780140283334"
    },
    {
        "title": "LIFE OF PI",
        "author": "YANN MARTEL",
        "year": "2006",
        "ISBN": "9780770430078"
    },
    {
        "title": "DUNE: DELUXE EDITION",
        "author": "FRANK HERBERT",
        "year": "2019",
        "ISBN": "9780593099322"
    },
    {
        "title": "THE FELLOWSHIP OF THE RING",
        "author": "J.R.R TOLKIEN",
        "year": "2012",
        "ISBN": "9780007488315"
    }
]



def display_book(book_info):
    """
    This function will display the
    Title, Author, Year and ISBN of the book.
    This is called if the system finds the book requested by the user in the library.
    """
    print(f"Title: {book_info['title']}")
    print(f"Author: {book_info['author']}")
    print(f"Year: {book_info['year']}")
    print(f"ISBN: {book_info['ISBN']}")

def borrow_book(book_info):
    print(f"You have borrowed '{book_info['title']}'. Enjoy your reading!")


def add_book():
    



# Get user input for book title
user_borrow = input("What book do you want to borrow? ").strip().upper()

# Check for the book by title
book_found = False

for book in library:
    if book['title'].upper() == user_borrow:
        display_book(book)
        borrow_book(book)
        book_found = True
        break

if not book_found:
    print("That book is unavailable, please try again.")