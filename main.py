import logging
from endpoints.bookname_api import search_book
from library.personal_library import add_personal_library

#logging of the mistakes errors being made
logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

#TODO: Maak een inlog page (maybe just use an username only, without passwords)






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

#TODO: maak menu page

def main_menu():
    print("|------- Your Personal Library -------|")
    username = input("Enter your username: ")
    print(f"Welcome {username}!")

    while True: #The menu shown
        print("1. Look for a book.")
        print("2. Look for an author.")
        print("3. Your Library.")
        print("4. Exit.")

        try: #checking if the choice is a number
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number.")
            logging.warning(f"Invalid choice. (no number entered)")
            continue

        if choice == 1:
            #look for book with search api
            books = search_book_query()
            chosen_book = book_choice(books)

            if chosen_book is not None:
                print("1. Add to your library.")
                print("2. Look at author.")
                print("3. Back to main menu.")
                book_menu = input("Enter your choice: ")

                if book_menu == "1":
                    add_personal_library(chosen_book)
                    print(f"Book added to {username}'s library!")
                if book_menu == "2":
                    #TODO: add search author api (temporary pass)
                    pass
                if book_menu == "3":
                    pass



        elif choice == 2: # searching for an author
        #TODO: look for author Api
            pass
        elif choice == 3:
        #TODO: library with choices, favourite page?
            pass
        elif choice == 4:
            print(f"Goodbye {username}!")
            break
        else:
            print("Invalid choice. Please try again.")
            logging.warning(f"Invalid choice. (invalid menu number)")


main_menu()