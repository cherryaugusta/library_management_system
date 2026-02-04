from library import Library  # Import the Library class from library.py
from member import Member  # Import the Member class from member.py

def main():
    # Create a Library instance
    my_library = Library("City Library")

    # Create some books
    book1 = my_library.create_book("The Catcher in the Rye", "J.D. Salinger", "12345")
    book2 = my_library.create_book("1984", "George Orwell", "67890")
    book3 = my_library.create_book("To Kill a Mockingbird", "Harper Lee", "11223")

    # Add books to the library
    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)

    # Create some library members
    member1 = Member("Alice", "1")  # Create member directly instead of using create_member
    member2 = Member("Bob", "2")    # Create member directly instead of using create_member

    # Register members with the library
    my_library.register_member(member1)
    my_library.register_member(member2)

    # Member borrows a book
    member1.borrow_book(book1)
    member2.borrow_book(book2)

    # Display information
    my_library.show_books()  # Display all books
    my_library.show_members()  # Display all members

    # Show member borrowing details
    member1.show_borrowed_books()
    member2.show_borrowed_books()

if __name__ == "__main__":
    main()
