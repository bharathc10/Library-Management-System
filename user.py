class User:
    """
    Represents a library user.

    Attributes:
        name (str): The name of the user.
        email (str): The email address of the user.
        borrowed_books (list): A list of books that the user has borrowed.
    """
    
    def __init__(self, name, email):
        """
        Initializes a new User object with provided attributes.
        """
        
        self.name = name
        self.email = email
        self.borrowed_books = []

    def borrow_book(self, book):
        """
        Checks out a book and adds it to the user's list of borrowed books.
        """
        
        if book not in self.borrowed_books:
            self.borrowed_books.append(book)
            print(f"{self.name} has checked out the book: {book.title}")
        else:
            print(f"{self.name} has already borrowed the book: {book.title}")


    def return_book(self, book):
        """
        Returns a borrowed book and removes it from the user's list of borrowed books.
        """
        
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned the book: {book.title}")
        else:
            print(f"{self.name} did not borrow the book: {book.title}.")

    def user_collection(self):
        """
        Displays a list of books the user has borrowed.
        """
        
        if self.borrowed_books:
            print(f"{self.name}'s Borrowed Books:")
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")
        else:
            print(f"{self.name} has not borrowed any books.")