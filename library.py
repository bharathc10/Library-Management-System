class Library:
    def __init__(self):
        """
        Initialize a Library object with an empty catalog of books.
        """
        
        self.catalog = []

    def add(self, book):
        """
        Add a book to the library's catalog.
        """
        
        self.catalog.append(book)

    def borrow_book(self, user, book):
        """
        Allows a user to borrow a book from the library and removes it from the catalog.
        """
        
        if book in self.catalog:
            user.borrow_book(book)
            self.catalog.remove(book)
            print(f"{user.name} has borrowed {book.title}.")
        else:
            print("Book not found in the catalog.")

    def return_book(self, user, book):
        """
        Allow a user to return a borrowed book to the library and adds it to the catalog.
        """
        
        if book in user.borrow_book:
            self.catalog.append(book)
            user.return_book(book)
            print(f"{user.name} has returned {book.title}.")
        else:
            print("You didn't check out this book.")

    def display_catalog(self):
        """
        Display the details of all books available in the library's catalog.
        """
        
        for book in self.catalog:
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")