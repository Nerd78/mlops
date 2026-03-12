class Book:

    def __init__(self, title, author, pages, isbn, total_copies):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.total_copies = total_copies
        self.available_copies = total_copies
        self.waitlist = []

    def is_available(self):

        if self.available_copies > 0:
            return True
        else:
            return False

    def checkout_copy(self):

        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        else:
            return False

    def return_copy(self):

        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        else:
            return False

    def add_to_waitlist(self, user):

        if user not in self.waitlist:
            self.waitlist.append(user)
            return True
        else:
            return False

    def get_next_user(self):

        if len(self.waitlist) > 0:
            return self.waitlist.pop(0)
        else:
            return None

    def __str__(self):
        return f"{self.title} | Available: {self.available_copies}/{self.total_copies} | Waitlist: {len(self.waitlist)}"