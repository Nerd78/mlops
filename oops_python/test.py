from library import Library
from books import Book
from users import User


def main():

    # Create library
    library = Library()

    # Create books (with multiple copies)
    book1 = Book("Clean Code", "Robert Martin", 450, "101", 2)
    book2 = Book("Python Crash Course", "Eric Matthes", 500, "102", 1)

    # Add books to library
    print(library.add_book(book1))
    print(library.add_book(book2))

    print()

    # Create users
    user1 = User("Alex", 1)
    user2 = User("Sam", 2)
    user3 = User("John", 3)

    # Register users
    print(library.register_user(user1))
    print(library.register_user(user2))
    print(library.register_user(user3))

    print("\n--- Checkout Books ---")

    # Borrow books
    print(library.checkout_book(user1, book1))
    print(library.checkout_book(user2, book1))

    # This user should go to waitlist
    print(library.checkout_book(user3, book1))

    print("\n--- Library Status ---")
    library.show_available_books()

    print("\n--- Returning Book ---")

    # Returning a book should assign it to waitlisted user
    print(library.return_book(book1))

    print("\n--- Library Status After Return ---")
    library.show_available_books()


if __name__ == "__main__":
    main()