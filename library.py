books = {}

def add_book():
    isbn = input("Enter isbn: ")
    title = input("Enter title: ")
    author = input("Enter author: ")

    books[isbn] = {
        "title": title,
        "author": author,
        "availability": True
    }

    print("Book added successfully....")


def issue_book():
    isbn = input("Enter ISBN: ")

    if isbn in books:
        if books[isbn]["availability"] == True:
            borrower = input("Enter borrower name: ")
            date = input("Enter issue date: ")

            books[isbn]["availability"] = False
            books[isbn]["borrower"] = borrower
            books[isbn]["date"] = date

            print("Book issued successfully....")
        else:
            print("Book is not available....")
    else:
        print("Book not found....")


def return_book():
    isbn = input("Enter ISBN: ")

    if isbn in books:
        if books[isbn]["availability"] == False:
            books[isbn]["availability"] = True
            books[isbn]["borrower"] = None
            books[isbn]["date"] = None

            print("Book returned successfully...")
        else:
            print("Book is already available.")
    else:
        print("Book not found...")


def search_book():
    keyword = input("Enter title or author: ")
    found = False

    for isbn in books:
        if keyword in books[isbn]["title"] or keyword in books[isbn]["author"]:
            print("ISBN:", isbn)
            print("Title:", books[isbn]["title"])
            print("Author:", books[isbn]["author"])
            print("Available:", books[isbn]["availability"])
            found = True

    if not found:
        print("Book not found...")


def view_catalog():
    print("\nISBN\tTitle\tAuthor\tAvailable")

    for isbn in books:
        print(isbn, "\t",
            books[isbn]["title"], "\t",
            books[isbn]["author"], "\t",
            books[isbn]["availability"])


while True:
    print("\n***📚 Library Management System 📚***")
    print("\n1.Add Book")
    print("2.Issue Book")
    print("3.Return Book")
    print("4.Search Book")
    print("5.View Catalog")
    print("6.Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        issue_book()

    elif choice == "3":
        return_book()

    elif choice == "4":
        search_book()

    elif choice == "5":
        view_catalog()

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice...")