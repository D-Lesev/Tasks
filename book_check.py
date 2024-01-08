import json
import os

_CURRENT_DB = ""


def create_book(author, book_name, read=False):
    current_db = {author: {book_name: read}}

    try:
        with open(_CURRENT_DB, "r") as f:
            cont = json.load(f)

            if author in cont.keys():
                if book_name in cont[author].keys():
                    print("Your book is already in")
                else:
                    cont[author][book_name] = read
            else:
                cont[author] = {book_name: read}

            with open(_CURRENT_DB, "w") as f:
                json.dump(cont, f)
    except json.JSONDecodeError:
        with open(_CURRENT_DB, "w") as f:
            json.dump(current_db, f)


def edit_book(book_name):
    with open(_CURRENT_DB, "r") as f:
        cont = json.load(f)

    found_book = False
    for author, books in cont.items():
        for book in books:
            if book_name.lower() == book.lower():
                found_book = True
                print("[!] Your book was found.")
                is_read = cont[author][book]
                if not is_read:
                    print("Currently you did not read this book.")
                    response = input("Do you read this book already? Do you want to make it True? (Yes || No)\n")
                    if response.lower() == "yes":
                        cont[author][book] = True

                break
        if found_book:
            break

    with open(_CURRENT_DB, "w") as f:
        json.dump(cont, f)


def delete_book(book_name):
    with open(_CURRENT_DB, "r") as f:
        cont = json.load(f)

    found_book = False
    for author, books in cont.items():
        for book in books:
            if book_name.lower() == book.lower():
                del cont[author][book]
                if len(cont[author]) == 0:
                    del cont[author]
                found_book = True
                print("[+] Your book has been deleted")
                break
        if found_book:
            with open(_CURRENT_DB, "w") as f:
                json.dump(cont, f)
            break


def search_book(book_name):
    with open(_CURRENT_DB, "r") as f:
        content = json.load(f)

    found_book = False
    for books in content.values():
        for book in books:
            if book_name.lower() == book.lower():
                found_book = True
                break
        if found_book:
            break
    print("[-] You don't have this book") if not found_book else print("[+] You found your book!")


def create_home_lib():
    global _CURRENT_DB

    files = os.listdir("./")

    for i in files:
        if i.endswith(".json"):
            _CURRENT_DB = i
            print("You have already created a home library\n[!] Entering this DB.")
            break

    if _CURRENT_DB == "":
        name_of_home_lib = input("Enter your home DB:\n")

        with open(f"{name_of_home_lib}.json", "w") as file:
            _CURRENT_DB = f"{name_of_home_lib}.json"
            print("[+] Your DB has been created.")


def reading_the_db():
    # Reading from the JSON file
    ...


def main():
    print("Hello! Welcome to Home Library\nYou can safe your books here.\n")
    create_home_lib()
    print("\nPlease enter number of what you want:\n")
    print("1. Create book\n"
          "2. Edit book\n"
          "3. Delete book\n"
          "4. Search book\n"
          "5. Print current library")
    valid_choice = input(">>>\t")

    if valid_choice == "1":
        stop = False
        while not stop:
            author_name = input("Enter the name of the author:\n")
            book_name = input("Enter the name of the book:\n")
            create_book(author_name, book_name)

            print("Do you want to add more books? (Yes || No)\n")
            response = input(">>\t").lower()

            if response == "no":
                stop = True

    elif valid_choice == "2":
        stop = False
        while not stop:
            book_to_edit = input("Which book do you want to edit?\t")
            edit_book(book_to_edit)

            print("[!] You change the status of your book!\nDo you want to change another book? (YES || NO)")
            response = input(">>\t")

            if response.lower() == "no":
                stop = True

    elif valid_choice == "3":
        stop = False
        while not stop:
            searched_book = input("What book do you want to delete:\t").lower()
            delete_book(searched_book)

            print("Do you want to delete more books? (Yes || No)\n")
            response = input(">>\t").lower()

            if response == "no":
                stop = True

    elif valid_choice == "4":
        stop = False
        while not stop:
            searched_book = input("What book are you looking for:\t").lower()
            search_book(searched_book)

            print("Do you want to search for another book? (Yes || No)\n")
            response = input(">>\t").lower()

            if response == "no":
                stop = True

    elif valid_choice == "5":
        # TODO: 1. Print each author with it's book and if this book was read
        #       2. Make something like a table with Author, Book Name and if the book is read (YES/NO)
        #       3. If all of the above is working, make sure that we can print all books sorted by name of author
        #       and for each author the books are also sorted by name
        ...

    else:
        ...


if __name__ == "__main__":
    main()
