from api import search_book
from personal_library import write_to_personal_library, open_personal_library

user_action = input("What do you want to do?")

#ToDo: Maak een inlog page
#ToDo:

if(user_action == "search"):
    book_input = input("what book do you want? ")
    field_input = input("what field do you want? ")
    search_result = search_book(book_input, field_input)
    write_to_personal_library(search_result)
elif(user_action == "open library"):
    print("opening library")
    print(open_personal_library())

