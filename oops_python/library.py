from loan import Loan


class Library:

    def __init__(self):
        self.books = []
        self.users = []
        self.loans = []

    def add_book(self, book):

        if book not in self.books:
            self.books.append(book)
            return f"{book.title} added to library"

        else:
            return f"{book.title} already exists in library"

    def register_user(self, user):

        if user not in self.users:
            self.users.append(user)
            return f"User {user.name} registered successfully"

        else:
            return f"User {user.name} already registered"

    def checkout_book(self, user, book):

        if book.is_available():

            if book.checkout_copy():

                loan = Loan(user, book)
                self.loans.append(loan)

                return f"{user.name} borrowed {book.title}"

            else:

                if book.add_to_waitlist(user):
                    return f"{user.name} added to waitlist for {book.title}"

                else:
                    return f"{user.name} is already in waitlist"

        else:
            return f"{book.title} is currently not available"

    def return_book(self, book):

        for loan in self.loans:

            if loan.book == book and loan.return_date is None:

                if loan.close_loan():

                    next_user = book.get_next_user()

                    if next_user is not None:

                        new_loan = Loan(next_user, book)
                        self.loans.append(new_loan)

                        return f"{book.title} returned and automatically assigned to {next_user.name}"

                    else:

                        book.return_copy()
                        return f"{book.title} returned successfully"

                else:
                    return "Loan already closed"

            else:
                continue

        else:
            return "Active loan record not found"

    def show_available_books(self):

        available_books = []

        for book in self.books:

            if book.is_available():
                available_books.append(book)

            else:
                continue

        if len(available_books) > 0:

            for book in available_books:
                print(book)

        else:
            print("No books available in library")