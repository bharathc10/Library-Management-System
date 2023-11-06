class Book:
    """
    Represents a book in a library.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        isbn (str): The International Standard Book Number (ISBN) of the book.
        genre (str): The genre of the book.
        pub_year (int): The publication year of the book.
        avail_status (str): The availability status of the book.

    Optional Attributes:
        language (str): The language of the book.
        rating (float): The rating of the book.
        npage (int): The number of pages in the book.
        condition (str): The condition of the book.
        location (str): The location of the book in the library.
        borrower (str): The name of the borrower if the book is checked out.
    """
    
    def __init__(self, title, author, isbn, genre, pub_year, avail_status):
        """
        Initializes a Book object with the provided attributes.
        """
        
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.pub_year = pub_year
        self.avail_status = avail_status

        # Optional attributes
        opt_name = {
            'language': None,
            'rating': None,
            'npage': None,
            'condition': None,
            'location': None,
            'borrower': None
        }
        # Now we only need to edit this dictionary to modify attributes
        for key, value in opt_name.items():
            setattr(self, key, value)

    def book_details(self):
        """
        Displays the details of the book using the initialised parameters.
        """
        print("Title:", self.title)
        print("Author:", self.author)
        print("ISBN:", self.isbn)
        print("Genre:", self.genre)
        print("Publication Year:", self.pub_year)
        print("Availability Status:", self.avail_status)

        opt_labels = {
            'language': 'Language',
            'rating': 'Rating',
            'npage': 'Number of Pages',
            'condition': 'Condition',
            'location': 'Location',
            'borrower': 'Borrower'
        }

        for name, label in opt_labels.items():
            value = getattr(self, name)
            if value is not None:
                print(f"{label}:", value)

    
    def availabilty(self):
        """
        Checks the availablity of the book.
        """
        return self.avail_status == "Available"
    
    def borrow(self, borrower_name):
        """
        Updates the availability when 
        """
        if self.availability():
            self.avail_status = "Checked Out"
            self.borrower = borrower_name
            print(f"{self.title} has been checked out by {self.borrower}.")
        else:
            print(f"{self.title} is not available for checkout.")

    def book_return(self):
        if not self.availability():
            self.avail_status = "Available"
            borrower_name = self.borrower
            self.borrower = None
            print(f"{self.title} has been returned by {borrower_name}.")
        else:
            print(f"{self.title} is already available.")