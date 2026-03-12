from datetime import datetime

class Loan:

    def __init__(self, user, book):
        self.user = user
        self.book = book
        self.checkout_date = datetime.now()
        self.return_date = None

    def close_loan(self):
        self.return_date = datetime.now()

    def __str__(self):
        return f"{self.book.title} borrowed by {self.user.name}"