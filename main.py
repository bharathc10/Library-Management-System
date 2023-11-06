"""
Library Management System

This program is a simple library management system that allows users to add books to a library catalog, search for books in the catalog, borrow books, return books, and display the catalog.

Classes:
Book: Represents a book in the library.
User: Represents a library user.
Catalog: Manages the catalog of available books.
Library: Manages the library's catalog and user interactions.

Functions:
main(): The main function that serves as the entry point of the program. It provides a menu for users to interact with the library system.

Usage:
1. Run this program.
2. Choose from the menu options to add books, search the catalog, borrow books, return books, or display the catalog.
3. Follow the on-screen instructions for each option.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from book import Book
from user import User
from catalog import Catalog
from library import Library

def main():
    library = Library()
    catalog = Catalog()

    while True:
        print("\nLibrary Management System")
        print("1. Add a Book")
        print("2. Search for Books")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Display Catalog")
        print("6. Quit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            # Add a book to the library's catalog
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            genre = input("Enter genre: ")
            pub_year = input("Enter publication year: ")
            avail_status = "Available"
            book = Book(title, author, isbn, genre, pub_year, avail_status)
            library.add(book)
            catalog.add(book)
            print(f"{book.title} has been added to the catalog.")

        elif choice == "2":
            # Search for books in the catalog
            search_type = input("Search by (Title/Author/ISBN): ").lower()
            if search_type == "title":
                title = input("Enter book title: ")
                catalog.title_search(title)
            elif search_type == "author":
                author = input("Enter author name: ")
                catalog.author_search(author)
            elif search_type == "isbn":
                isbn = input("Enter ISBN: ")
                catalog.isbn_search(isbn)
            else:
                print("Invalid search type. Please use Title, Author, or ISBN.")

        elif choice == "3":
            # Borrow a book
            user_name = input("Enter your name: ")
            user_email = input("Enter your email: ")
            user = User(user_name, user_email)
            catalog.display_books()
            book_title = input("Enter the title of the book you want to borrow: ")
            for book in library.catalog:
                if book.title == book_title:
                    library.borrow_book(user, book)
                    break

        elif choice == "4":
            # Return a book
            user_name = input("Enter your name: ")
            user_email = input("Enter your email: ")
            user = User(user_name, user_email)
            user.user_collection()
            book_title = input("Enter the title of the book you want to return: ")
            for book in user.borrowed_books:
                if book.title == book_title:
                    library.return_book(user, book)
                    break

        elif choice == "5":
            # Display the catalog
            catalog.display_books()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
