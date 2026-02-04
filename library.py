from book import Book  # Import the Book class from book.py
from member import Member  # Import the Member class from member.py

class Library:
    def __init__(self, name):
        self.name = name  # Library name
        self.books = []  # List to store available books
        self.members = []  # List to store registered members
    
    def create_book(self, title, author, isbn):
        """Create a book object and return it."""
        return Book(title, author, isbn)
    
    def add_book(self, book):
        """Add a book to the library's collection."""
        self.books.append(book)
    
    def register_member(self, member):
        """Register a member to the library."""
        self.members.append(member)
    
    def show_books(self):
        """Display all books available in the library."""
        print("\nBooks in the Library:")
        for book in self.books:
            print(f"- {book.title} by {book.author} (ISBN: {book.isbn})")
    
    def show_members(self):
        """Display all members of the library."""
        print("\nLibrary Members:")
        for member in self.members:
            print(f"- {member.name} (Member ID: {member.member_id})")