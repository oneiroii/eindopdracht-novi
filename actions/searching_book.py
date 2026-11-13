import logging
from endpoints.book_search_api import search_book

#search book
def search_book_query(): # they enter a book and they see results
    title = input("Enter your book title: ")
    if title.strip() == "":
        print("Please enter a book title.")
        logging.warning(f"Empty string waring.")
        return []
    books = search_book(title)

    for number, book in enumerate(books, start=1):
        author = book.get("author_name", ["Unknown author"])
        year_published = book.get("first_publish_year", "unknown year")
        print(f"{number}. {book['title']} - {author[0]} ({year_published}) " )
    return books

def book_choice(books): #with this you can choose a book
    if not books:
        print("No books found :(")
        logging.warning(f"Search found no books")
        return None

    while True:
        book_number = int(input("Choose the book number or go back with 0."))
        try:
            book_number = int(book_number) #check if int
        except ValueError:
            print("Please enter a number!")
            logging.warning(f"Invalid choice, no number.")

        if book_number == 0:
            break
        elif 1 <= book_number <= len(books):
            chosen_book = books[book_number-1]
            author = chosen_book.get("author_name", ["Unknown author"])[0]
            print(f"Book chosen: {chosen_book['title']} by {author}")
            return chosen_book
        else:
            print(f"invalid choice. Please enter a number from 0 to {len(books)}.")
            logging.warning(f"Invalid choice. (invalid book number)")