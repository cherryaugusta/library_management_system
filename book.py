class Book:
    def __init__(self, title, author, isbn):
        self.title = title  # Title of the book
        self.author = author  # Author of the book
        self.isbn = isbn  # ISBN of the book
        self.is_borrowed = False  # Flag to check if the book is borrowed

    def borrow(self):
        """Mark the book as borrowed."""
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False
    
    def return_book(self):
        """Mark the book as returned."""
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False