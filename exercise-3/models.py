from pydantic import BaseModel


class Book(BaseModel):
    book_id: int
    title: str
    author: str
    published_year: int
    category: str
    rating: float
    availability: bool
    pages: int
    isbn: str
    uuid: str
