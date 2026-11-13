import json
import logging

THE_LIBRARY = "data/personal_library.json"

def open_personal_library(): #read/open the library
    try: #avoid the error with an except!
        with open(THE_LIBRARY, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logging.warning(f"Could not read library, starting empty: {e}")
        return []

def save_personal_library(library):
    with open(THE_LIBRARY, "w") as file:
        json.dump(library, file)

def add_personal_library(book):
    library = open_personal_library()
    if book in library:
        print(f"This book is already in the library!")
        logging.warning(f"{book} was already in library")
    else:
        library.append(book)
        save_personal_library(library)
        print(f"{book} added to library!")

def delete_book(book_number):
    library = open_personal_library()

    removed_book = library.pop(book_number - 1)
    save_personal_library(library)
    logging.info(f"Removed book: {removed_book}")
    return removed_book
