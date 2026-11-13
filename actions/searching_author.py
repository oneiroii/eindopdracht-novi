import logging
from endpoints.author_search_api import search_for_author_with_api, show_author_works_with_api

def search_author():
    insert_author = input("What author are you looking for? : ")

    if insert_author.strip() == "":
        print("String empty. Please enter a valid author")
        logging.warning("Invalid author. Empty string.")
        return None

    return show_author_and_books(insert_author)


def show_author_and_books(author_name): #as it says show the author and all the books
    searched_author = search_for_author_with_api(author_name)

    if not searched_author:
        print(f"Author {author_name} not found. Please try again.")
        logging.warning(f"Author {author_name} not found.")
        return None

    first_result = searched_author[0]
    author = first_result.get("name", "Unknown author")
    top_work = first_result.get("top_work", "unknown")
    birth_date = first_result.get("birth_date", "unknown")
    author_key = first_result.get("key")

    author_books = show_author_works_with_api(author_key)
    for book in author_books:
        book["author_name"] = [author]

    print(f"Author: {author} ({birth_date}), Most popular: {top_work}")
    for number, book in enumerate(author_books, start=1):
        print(f"{number}. {book['title']}")

    return author_books

