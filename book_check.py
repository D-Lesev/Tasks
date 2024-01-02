import json
import os

_CURRENT_DB = ""


# {avtor: { {kniga_ime: xyz, chetena: tr/fals}
#           {kniga_ime: xyz2, chetna: tr}}
#  avtor2: ............... }

# TODO: Създаване
#       Изтриване
#       Редактиране
#       Търсене -> Автор / Име на книга

# def load_current_db(db_filename):
#     content = {}
#     try:
#         with open(db_filename, "r") as file:
#             file_content = file.read()
#             if file_content:
#                 content = json.loads(file_content)
#             else:
#                 print(f"Error: File {db_filename} is empty.")
#     except FileNotFoundError:
#         print(f"Error: File {db_filename} not found. Make sure the file exists.")
#     except json.JSONDecodeError:
#         print(f"Error: Unable to decode JSON in file {db_filename}. Make sure the file contains valid JSON data.")
#     return content


def create_book(author, book_name, read=False):
    current_db = {author: {book_name: read}}

    print(current_db)

    try:
        with open(_CURRENT_DB, "r") as f:
            cont = json.load(f)

            for authors in cont.keys():
                if author in authors:
                    if book_name in cont[author].keys():
                        print("Your book is already in")
                    else:
                        cont[author][book_name] = read

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

    if _CURRENT_DB is None:
        name_of_home_lib = input("Enter your home DB:\n")

        with open(f"{name_of_home_lib}.json", "w") as file:
            _CURRENT_DB = f"{name_of_home_lib}.json"
            print("[+] Your DB has been created.")


def reading_the_db():
    # Reading from the JSON file
    ...


def main():
    print("Hello! Welcome to Home Library\nYou can safe your books here.")
    print()
    create_home_lib()
    print()
    print("Please enter number of what you want:\n")
    print("1. Create book")
    print("2. Edit book")
    print("3. Delete book")
    print("4. Search book")
    valid_choice = input(">>>\n")

    if valid_choice == "1":
        author_name = input("Enter the name of the author:\n")
        book_name = input("Enter the name of the book:\n")
        create_book(author_name, book_name)


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