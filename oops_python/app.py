from fastapi import FastAPI
from pydantic import BaseModel

from library import Library
from books import Book
from users import User

app = FastAPI()

library = Library()


class BookRequest(BaseModel):
    title: str
    author: str
    pages: int
    isbn: str
    copies: int


class UserRequest(BaseModel):
    name: str
    user_id: int


class CheckoutRequest(BaseModel):
    user_id: int
    isbn: str


class ReturnRequest(BaseModel):
    isbn: str


@app.post("/books")
def add_book(book: BookRequest):

    new_book = Book(
        book.title,
        book.author,
        book.pages,
        book.isbn,
        book.copies
    )

    result = library.add_book(new_book)

    return {"message": result}


# Register User
@app.post("/users")
def register_user(user: UserRequest):

    new_user = User(user.name, user.user_id)

    result = library.register_user(new_user)

    return {"message": result}


@app.post("/checkout")
def checkout_book(data: CheckoutRequest):

    user = next((u for u in library.users if u.user_id == data.user_id), None)
    book = next((b for b in library.books if b.isbn == data.isbn), None)

    if user and book:

        result = library.checkout_book(user, book)

        return {"message": result}

    else:
        return {"error": "User or Book not found"}


@app.post("/return")
def return_book(data: ReturnRequest):

    book = next((b for b in library.books if b.isbn == data.isbn), None)

    if book:

        result = library.return_book(book)

        return {"message": result}

    else:
        return {"error": "Book not found"}


# Show Books
@app.get("/books")
def show_books():

    books = []

    for book in library.books:

        books.append({
            "title": book.title,
            "author": book.author,
            "isbn": book.isbn,
            "available": book.available_copies,
            "total": book.total_copies,
            "waitlist": len(book.waitlist)
        })

    return books