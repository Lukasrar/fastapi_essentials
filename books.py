from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {'title': "title one", "author": 'Author one', 'category': 'science'},
    {'title': "title two", "author": 'Author two', 'category': 'science'},
    {'title': "title three", "author": 'Author three', 'category': 'history'},
    {'title': "title four", "author": 'Author four', 'category': 'math'},
    {'title': "title five", "author": 'Author five', 'category': 'terror'},
    {'title': "title six", "author": 'Author two', 'category': 'science'}
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_title}")
async def get_book_by_name(book_title):
    selectedBook = None
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            selectedBook = book
            break

    return selectedBook  

@app.get('/books/')
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.get('/books/{book_author}/')
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.post('/books/create_book')
async def create_book(new_book = Body()):
    BOOKS.append(new_book)

@app.put('/books/update_book')
async def update_book(updated_book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book

@app.delete('/books/delete_book/{book_title}')
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break

@app.get('/books/by_author/{author_name}')
async def get_books_by_author(author_name: str):
    return list(filter(lambda b: b.get('author').casefold() == author_name.casefold(), BOOKS))
