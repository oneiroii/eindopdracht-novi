import logging
from endpoints.authorsearch_api import search_for_author, show_author_works
from endpoints.bookname_api import search_book

def print_author(): #get the author
    insert_author = input("What author are you looking for? : ")

    if not insert_author:
        print("Please enter an author name.")
        logging.warning("Invalid author. Empty string.")
        return None

    searched_author = search_for_author(insert_author)
    first_result = searched_author[0]

    if not searched_author:
        print(f"Author {insert_author} not found. Please try again.")
        logging.warning(f"Author {insert_author} not found.")
        return None

    author = first_result.get("name")
    top_work = first_result.get("top_work")
    birth_date = first_result.get("birth_date")
    author_key = first_result.get("key")

    author_books = show_author_works(author_key)

    date_created = first_result.get("value")
    #TODO: FIX SEEING OTHER LANGUAGES

    if insert_author == "":
        print("String empty. Please enter a valid author")
        logging.warning(f"Invalid author. Empty string.")
    elif not searched_author:
        print(f"Author {insert_author} not found. Please try again.")
        logging.warning(f"Author {insert_author} not found.")
    else:
        print(f"Author: {author}({birth_date}), Most popular: {top_work}")

        for number, titles in enumerate(show_author_works(author_key), start=1):
            #TODO: maybe fix not seeing the dates
            print(f"{number}. {titles['title']} ({date_created}) ")
    return author_books

def choose_book_from_author(author_books): #choose a book or small menu
    author_menu = int(input("Choose a book number or go back with 0. "))
    book_info = search_book(author_books)
    if author_menu == 0:
        return None
    elif author_menu <= 0 or author_menu <= len(author_books):
        chosen_book = author_books[author_menu-1]
        return chosen_book


#print(choose_book_from_author(print_author()))