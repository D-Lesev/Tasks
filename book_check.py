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
    ...


def delete_book(book_name):
    ...


def search_book(book_name):
    ...


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
            flag = input(">>\t").lower()

            if flag == "no":
                stop = True

    elif valid_choice == "2":
        # TODO: 1. Search book by book name
        #           - if we have the same book name -> show all possible authors
        #       2. To choose with numbers
        #       3. After choosing the item we need to choose what to edit -> for now only if it was read (Yes/No)
        #       4. Write the new status to the current book
        ...

    elif valid_choice == "3":
        # TODO: 1. Search book by book name
        #       2. Delete the the book which we choose
        ...

    elif valid_choice == "4":
        # TODO: 1. Search book by book name
        #       2. Show if we have the searched book
        #       3. If not, ask for new search or no
        ...

    elif valid_choice == "5":
        # TODO: 1. Print each author with it's book and if this book was read
        #       2. Make something like a table with Author, Book Name and if the book is read (YES/NO)
        #       3. If all of the above is working, make sure that we can print all books sorted by name of author
        #       and for each author the books are also sorted by name
        ...

    else:
        ...


def test_f():
    author_name = input("Enter the name of the author:\n")
    book_name = input("Enter the name of the book:\n")
    create_book(author_name, book_name)
    # try:
    #     with open("books.json", "r") as f:
    #         cont = json.load(f)
    #         return cont
    # except json.JSONDecodeError:
    #     print("Empty file")
    #
    # cur = {
    #     "Kevin Lin": {
    #         "Klipodmv": False,
    #         "Tesmvnir": True,
    #         "POldivm": False
    #     },
    #     "Polin Lkil": {
    #         "Iowemv": False,
    #         "Wcmbtim": True
    #     }
    # }


if __name__ == "__main__":
    main()
    # test_f()