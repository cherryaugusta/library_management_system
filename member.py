
class Member:
    def __init__(self, name, member_id):
        self.name = name  # Name of the library member
        self.member_id = member_id  # Member's unique ID
        self.borrowed_books = []  # List of borrowed books by the member
    
    def borrow_book(self, book):
        """Allow a member to borrow a book."""
        if book.borrow():  # If the book is available to borrow
            self.borrowed_books.append(book)
            print(f"{self.name} successfully borrowed {book.title}")
        else:
            print(f"{book.title} is already borrowed.")
    
    def return_book(self, book):
        """Allow a member to return a borrowed book."""
        if book in self.borrowed_books:
            if book.return_book():  # Return the book to the library
                self.borrowed_books.remove(book)
                print(f"{self.name} returned {book.title}")
        else:
            print(f"{self.name} didn't borrow {book.title}.")
    
    def show_borrowed_books(self):
        """Show all books borrowed by the member."""
        if self.borrowed_books:
            print(f"\n{self.name}'s Borrowed Books:")
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author} (ISBN: {book.isbn})")
        else:
            print(f"{self.name} has not borrowed any books.")