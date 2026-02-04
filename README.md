# Library Management System

This is a simple Library Management System designed using Object-Oriented Programming (OOP) principles in Python. The application allows managing books, members, and the borrowing process. The core OOP principles used include encapsulation, inheritance, and polymorphism.

## Project Structure

- `main.py`: The entry point of the application. It initializes the library, adds books, registers members, and manages book borrowing and returning.
- `library.py`: Contains the `Library` class, which manages the library's collection of books and members.
- `book.py`: Defines the `Book` class, which represents the books in the library.
- `member.py`: Defines the `Member` class, which represents the library members and their interactions with books.

## Features

- Create and manage books and members.
- Members can borrow and return books.
- Display the list of all available books and registered members.
- Show a member's borrowed books.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/library-management-system.git
   cd library-management-system
   ```

2. **Run the application**:
   - Make sure you have Python installed (Python 3.6+ recommended).
   - Run the `main.py` file to execute the library management system:

     ```bash
     python main.py
     ```

## Expected Output

```
Books in the Library:
- The Catcher in the Rye by J.D. Salinger (ISBN: [ISBN Number])
- 1984 by George Orwell (ISBN: [ISBN Number])
- To Kill a Mockingbird by Harper Lee (ISBN: [ISBN Number])

Library Members:
- Alice (Member ID: 1)
- Bob (Member ID: 2)

Alice successfully borrowed The Catcher in the Rye
Bob successfully borrowed 1984

Alice's Borrowed Books:
- The Catcher in the Rye by J.D. Salinger (ISBN: [ISBN Number])

Bob's Borrowed Books:
- 1984 by George Orwell (ISBN: [ISBN Number])
```

## OOP Concepts Demonstrated

### 1. **Encapsulation**:

- The `Book`, `Member`, and `Library` classes encapsulate their data and functionality. Access to their internal states is controlled through methods such as `borrow_book`, `return_book`, `show_books`, and `show_members`.

### 2. **Inheritance**:

- Although not explicitly shown in this basic example, inheritance could be easily introduced. For instance, creating specialized `EBook` or `AudioBook` classes that inherit from `Book`, or creating different types of members like `PremiumMember`.

### 3. **Polymorphism**:

- Polymorphism can be implemented by overriding methods in subclasses. For example, the `borrow` method could behave differently for `EBook` and `AudioBook` classes by customizing how each type of book is borrowed.

## Disclaimer

This project is designed **for educational purposes** only. It is a simple implementation intended to showcase Object-Oriented Programming (OOP) concepts in Python, specifically **encapsulation**, **inheritance**, and **polymorphism**. The project does not represent a fully-functional or production-ready library management system, and should not be used for real-world applications.

This project is also part of a **portfolio showcase** to demonstrate my understanding of OOP principles and Python programming. It is not intended for commercial use or professional deployment.

## Authors

- **Cherry Augusta** - [GitHub Profile Link](https://github.com/cherryaugusta)

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/cherryaugusta/library_management_system/blob/main/LICENSE) file for details.
