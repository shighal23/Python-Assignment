"""
============================================================================================
Library System - Python Assignment
============================================================================================
Name: Anshika
Date: 21 Nov 2025
Assignment: Library Management System

import json

# ============================
# BOOK CLASS
# ============================
class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def borrow(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        self.available = True

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "available": self.available
        }

    @staticmethod
    def from_dict(data):
        return Book(
            title=data["title"],
            author=data["author"],
            isbn=data["isbn"],
            available=data["available"]
        )


# ============================
# MEMBER CLASS
# ============================
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book.isbn)
            return True
        return False

    def return_book(self, book):
        if book.isbn in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book.isbn)
            return True
        return False

    def to_dict(self):
        return {
            "name": self.name,
            "member_id": self.member_id,
            "borrowed_books": self.borrowed_books
        }

    @staticmethod
    def from_dict(data):
        m = Member(data["name"], data["member_id"])
        m.borrowed_books = data["borrowed_books"]
        return m


# ============================
# LIBRARY CLASS
# ============================
class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.load_data()

    # Add / Register
    def add_book(self, book):
        self.books.append(book)
        self.save_data()

    def register_member(self, member):
        self.members.append(member)
        self.save_data()

    # Find
    def find_book(self, isbn):
        return next((b for b in self.books if b.isbn == isbn), None)

    def find_member(self, member_id):
        return next((m for m in self.members if m.member_id == member_id), None)

    # Lend / Return
    def lend_book(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.find_book(isbn)

        if member and book:
            if member.borrow_book(book):
                self.save_data()
                return True
        return False

    def take_return(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.find_book(isbn)

        if member and book:
            if member.return_book(book):
                self.save_data()
                return True
        return False

    # JSON Save
    def save_data(self):
        try:
            data = {
                "books": [b.to_dict() for b in self.books],
                "members": [m.to_dict() for m in self.members]
            }
            with open("library_data.json", "w") as f:
                json.dump(data, f, indent=4)

        except Exception as e:
            print("Error saving data:", e)

    # JSON Load
    def load_data(self):
        try:
            with open("library_data.json", "r") as f:
                data = json.load(f)

            self.books = [Book.from_dict(d) for d in data.get("books", [])]
            self.members = [Member.from_dict(d) for d in data.get("members", [])]

        except FileNotFoundError:
            self.books = []
            self.members = []
        except Exception:
            print("Corrupted file. Starting fresh.")
            self.books = []
            self.members = []

    # Analytics
    def count_borrowed_books(self):
        return sum(not b.available for b in self.books)

    def library_report(self):
        return f"""
----- Library Report -----
Total Books: {len(self.books)}
Total Members: {len(self.members)}
Books Currently Borrowed: {self.count_borrowed_books()}
--------------------------
"""


# ============================
# MAIN PROGRAM (MENU)
# ============================
print("📚 Welcome to the Library Management System")

library = Library()

while True:
    print("\n--- MENU ---")
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. View Library Report")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Book Title: ")
        author = input("Author: ")
        isbn = input("ISBN: ")

        library.add_book(Book(title, author, isbn))
        print("Book added successfully.")

    elif choice == "2":
        name = input("Member Name: ")
        member_id = input("Member ID: ")

        library.register_member(Member(name, member_id))
        print("Member registered successfully.")

    elif choice == "3":
        member_id = input("Member ID: ")
        isbn = input("Book ISBN: ")

        if library.lend_book(member_id, isbn):
            print("Book borrowed successfully.")
        else:
            print("Borrow failed!")

    elif choice == "4":
        member_id = input("Member ID: ")
        isbn = input("Book ISBN: ")

        if library.take_return(member_id, isbn):
            print("Book returned successfully.")
        else:
            print("Return failed!")

    elif choice == "5":
        print(library.library_report())

    elif choice == "6":
        print("Exiting program... Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")
