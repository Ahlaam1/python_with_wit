import json
import os

class Book:
    def __init__(self, title, author, year, is_borrowed=False):
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = is_borrowed

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"You have successfully borrowed '{self.title}'.")
        else:
            print(f"'{self.title}' has already been borrowed.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"You have successfully returned '{self.title}'.")
        else:
            print("You cannot return a book you never borrowed!")


class Library:
    def __init__(self, filename="library_database.json"):
        self.filename = filename
        self.books = []
        self.load_data() 

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                try:
                    data = json.load(f)
                    for item in data:
                        book = Book(item["title"], item["author"], item["year"], item["is_borrowed"])
                        self.books.append(book)
                except json.JSONDecodeError:
                    print("File found but empty or corrupted, starting fresh.")
        else:
            print("No database file found. Starting with an empty library.")

    def save_data(self):
        with open(self.filename, "w") as f:
            json.dump([book.__dict__ for book in self.books], f, indent=4)

    def add_book(self, title, author, year):
        book = Book(title, author, year)
        self.books.append(book)
        self.save_data()
        print("You have successfully added a book to the library!")

    def list_books(self):
        if not self.books:
            print("No books in the library yet.")
            return False
        else:
            print("\nBooks in the library:")
            for i, book in enumerate(self.books, start=1):
                status = "Borrowed" if book.is_borrowed else "Available"
                print(f"{i}. {book.title} ({book.year}) by {book.author} - {status}")
            return True

    def borrow_book(self, index):
        if 0 <= index < len(self.books):
            self.books[index].borrow()
            self.save_data()
        else:
            print("Invalid book number.")

    def return_book(self, index):
        if 0 <= index < len(self.books):
            self.books[index].return_book()
            self.save_data()
        else:
            print("Invalid book number.")

library = Library()

while True:
    print("\n===== Islamic Library Menu =====")
    print("1. Add a Book")
    print("2. View All Books")
    print("3. Borrow a Book")
    print("4. Return a Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author: ")
        year = input("Enter year: ")
        library.add_book(title, author, year)

    elif choice == "2":
        library.list_books()

    elif choice == "3":
        if library.list_books():
            num = input("Enter book number to borrow: ")
            if num.isdigit():
                library.borrow_book(int(num) - 1)
            else:
                print("Please enter a valid number.")

    elif choice == "4":
        if library.list_books():
            num = input("Enter book number to return: ")
            if num.isdigit():
                library.return_book(int(num) - 1)
            else:
                print("Please enter a valid number.")

    elif choice == "5":
        print("Goodbye! May Allah increase you in knowledge.")
        break

    else:
        print("Invalid choice. Please select a number between 1 and 5.")
