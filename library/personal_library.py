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
    library_book = {
        "title": book["title"],
        "author": book.get("author_name", ["Unknown author"])[0],
        "key": book["key"],
        "status": "to be read"
    }
    library = open_personal_library()
    if library_book in library:
        print(f"This book is already in the library!")
        logging.warning(f"{library_book} was already in library")
    else:
        library.append(library_book)
        save_personal_library(library)
        print(f"{library_book['title']} added to library!")

def delete_book(book_number):
    library = open_personal_library()

    if book_number < 1 or book_number > len(library): #check numbers
        return None

    removed_book = library.pop(book_number - 1)
    save_personal_library(library)
    logging.info(f"Removed book: {removed_book}")
    return removed_book

def change_status(book_number, new_status):
    library = open_personal_library()

    if book_number < 1 or book_number > len(library):
        return None

    library[book_number - 1]["status"] = new_status
    save_personal_library(library)
    logging.info(f"Status changed: {library[book_number - 1]['title']} -> {new_status}")
    return library[book_number - 1]