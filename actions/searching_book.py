import logging
from endpoints.book_search_api import search_book

#search book
def search_book_query(): # they enter a book and they see results
    title = input("Enter your book title: ")
    books = search_book(title)

    for number, book in enumerate(books, start=1):
        author = book.get("author_name", ["Unknown author"])
        year_published = book.get("first_publish_year", "unknown year")
        print(f"{number}. {book['title']} - {author[0]} ({year_published}) " )
    return books

def book_choice(books): #with this the user can choose a book
    while True:
        book_number = int(input("Choose the book number or go back with 0."))
        if book_number == 0:
            break
        elif book_number > 0 or book_number < len(books):
            chosen_book = books[book_number-1]
            print(f"Book chosen: {chosen_book['title']} by {chosen_book['author_name']} ")
            return chosen_book
        else:
            print(f"invalid choice. Please enter a number from 0 to {len(books)}.")
            logging.warning(f"Invalid choice. (invalid book number)")