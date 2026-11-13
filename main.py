import logging

from actions.searching_author import choose_book_from_author, show_author_and_books, choose_book_from_author, \
    search_author
from library.personal_library import add_personal_library, open_personal_library, delete_book
from actions.searching_book import search_book_query, book_choice

#logging of the mistakes errors being made
logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

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
                    print("What's next?")

                if book_menu == "2":
                        author_chosen_name = chosen_book.get("author_name", ["Unknown author"])[0]
                        author_books = show_author_and_books(author_chosen_name)

                        if author_books:
                            picked_book = choose_book_from_author(author_books)

                            if picked_book:
                                add_choice = input(f"Add '{picked_book['title']}' to your library? (y/n): ")
                                if add_choice.lower() == "y":
                                    add_personal_library(picked_book)
                                elif add_choice.lower() == "n":
                                    pass
                                else:
                                    print("Invalid choice. Please try y or n")
                                    logging.warning(f"Invalid choice. (y/n answer)")
                if book_menu == "3":
                    pass

        elif choice == 2: # searching for an author
            author_books = search_author()

            if author_books:
                picked_book = choose_book_from_author(author_books)

                if picked_book:
                    add_choice = input(f"Add '{picked_book['title']}' to your library? (y/n): ")
                    if add_choice.lower() == "y":
                        add_personal_library(picked_book)



        elif choice == 3: #view the library
            library = open_personal_library()
            print(f"---{username}'s library ---")
            for number, item in enumerate(library, start=1): #show all the books
                author = item.get("author_name", ["Unknown author"])[0]
                print(f"{number}. {item['title']} - {author}")
            delete_menu = input("type 'delete' to delete an item or go back with 0.")
            #deleting menu
            if delete_menu == "delete":
                number_text = input("Which book number do you want to delete? (Choose number) ")
                try:
                    removed = delete_book(int(number_text))
                except ValueError:
                    print("Please enter a number.")
                    logging.warning(f"Invalid delete input (not a number): {number_text}")
                    continue

                if removed:
                    print(f"Deleted: {removed['title']}")
                else:
                    print("That book number doesn't exist.")
                    logging.warning(f"Invalid book number to delete: {number_text}")
            if delete_menu == "0":
                pass
        #exit
        elif choice == 4:
            print(f"Goodbye {username}!")
            break
        #error
        else:
            print("Invalid choice. Please try again.")
            logging.warning(f"Invalid choice. (invalid menu number)")


main_menu()