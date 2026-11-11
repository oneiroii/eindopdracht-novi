import json

THE_LIBRARY = "data/personal_library.json"

def open_personal_library(): #read/open the library
    try: #avoid the error with an except!
        with open(THE_LIBRARY, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_personal_library(library):
    with open(THE_LIBRARY, "w") as file:
        json.dump(library, file)

def add_personal_library(book):
    library = open_personal_library()
    library.append(book)
    save_personal_library(library)