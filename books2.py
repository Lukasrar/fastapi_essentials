from typing import Optional

from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from starlette import status
app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    release_date: int

    def __init__(self, id, title, author, description, rating, release_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.release_date = release_date


class BookRequest(BaseModel):
    id: Optional[int] = Field(description='Id not needed when creating a book', default=None)
    title: str = Field(min_length=3, max_length=20)
    author: str = Field(min_length=3, max_length=20)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=6)
    release_date: int = Field(gt=1999, lt=2030)

    class Config:
        json_schema_extra = {
            'example': {
                'title': 'A new book',
                'author': 'coding with lukas',
                'description': 'a new book',
                'rating': 5,
                'release_date': 2012
            }
        }

BOOKS = [
    Book(1, "Computer Science Pro", 'codewithlukas', 'A very nice Book', 5, 2012),
    Book(2, "JS like Pro", 'codewithlukas', 'great', 4, 2012),
    Book(3, "TS like Pro", 'codewithlukas', 'nice', 3, 2012),
    Book(4, "C++ like Pro", 'codewithlukas', 'average', 2, 2013),
    Book(5, "angular like Pro", 'FEacademy', 'average', 2, 2014),
]

@app.get('/books/release_date', status_code=status.HTTP_200_OK)
async def read_book_by_release_date(release_date: int = Query(gt=1999, lt=2030)):
    books_to_return = []
    for book in BOOKS:
        if book.release_date == int(release_date):
            books_to_return.append(book)
    return books_to_return

@app.get('/books/rating', status_code=status.HTTP_200_OK)
async def read_book_by_rating(book_rating: int = Query(gt=0, lt=7)):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return

@app.get('/books', status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS

@app.get(
    "/books/{book_id}",
    responses={404: {"description": "Book not found"}},
    status_code=status.HTTP_200_OK
)
async def get_book_by_id(book_id: int = Path(gt=0),):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail='book not found')

@app.post('/create-book', status_code=status.HTTP_201_CREATED)
async def create_book(new_book_request: BookRequest):
    new_book = Book(**new_book_request.model_dump())
    BOOKS.append(find_book_id(new_book))

def find_book_id(book: Book): 
    # if len(BOOKS) > 0:
    #     book.id = BOOKS[-1].id + 1
    # else:
    #     book.id = 1

    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1

    return book


@app.put(
    "/books/update_book",
    responses={404: {"description": "Book not found"}},
    status_code=status.HTTP_200_OK
)
async def update_book(book: BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            return BOOKS[i]
    raise HTTPException(404, detail='Book not found')
    

@app.delete(
    '/books/{book_id}',
    responses={404: {"description": "Book not found"}},
    status_code=status.HTTP_200_OK
)
async def delete_book(book_id: int = Path(gt=0)):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            return BOOKS
    raise HTTPException(404, detail='book not found')