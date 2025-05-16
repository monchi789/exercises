from fastapi import FastAPI
from typing import List, Set
from fetchers.openlibrary import fetch_openlibrary
from fetchers.googlebooks import fetch_googlebooks
from models import Book
from utils import create_book, SUBJECTS, BOOK_TARGET
import httpx
import asyncio

app = FastAPI()

@app.get("/books", response_model=List[Book])
async def get_books():
    books = []
    seen_keys: Set[tuple] = set()
    idx = 1

    async with httpx.AsyncClient() as client:
        while len(books) < BOOK_TARGET:
            tasks = []
            for subject in SUBJECTS:
                tasks.append(fetch_openlibrary(subject, client))
                tasks.append(fetch_googlebooks(subject, client))
            
            resuls = await asyncio.gather(*tasks)

            for result, source in zip(resuls, ["openlibrary", "googlebooks"] * len(SUBJECTS)):
                for entry in result:
                    book = create_book(entry, source, idx)
                    if book and (book.title.lower(), book.author.lower() not in seen_keys):
                        seen_keys.add((book.title.lower(), book.author.lower()))
                        books.append(book)
                        if len(books) >= BOOK_TARGET:
                            break
                        idx += 1
        
    return books
