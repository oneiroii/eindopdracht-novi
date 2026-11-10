import json


def write_to_personal_library(book_array):
    with open("json/personal_library.json", "a") as file:
        json.dump(book_array, file)

def open_personal_library():
    with open("json/personal_library.json", "r") as file:
        return json.load(file)