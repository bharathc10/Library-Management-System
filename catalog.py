class Catalog:
    def __init__(self):
        """
        Initialises a Catalog object with an empty list of available books.
        """
        
        self.available_books = []

    def add(self, book):
        """
        Adds a book to the catalog of available books.
        """
        
        self.available_books.append(book)

    def display_books(self):
        """
        Displays the details of all available books in the catalog.
        """
        
        for book in self.available_books:
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")

    def title_search(self, title):
        """
        Search for books in the catalog by title and display matching results.
        """
        
        match = [book for book in self.available_books if title in book.title]
        if match:
            for book in match:
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")
        else:
            print(f"No books found with the title: {title}")

    def author_search(self, author):
        """
        Search for books in the catalog by author and display matching results.
        """

        match = [book for book in self.available_books if author in book.author]
        if match:
            for book in match:
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")
        else:
            print(f"No books found by author: {author}")

    def isbn_search(self, isbn):
        """
        Search for books in the catalog by ISBN and display matching results.
        """
        
        match = [book for book in self.available_books if isbn == book.isbn]
        if match:
            for book in match:
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")
        else:
            print(f"No books found with ISBN: {isbn}")