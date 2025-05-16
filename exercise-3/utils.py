import random
import uuid
from models import Book


SUBJECTS = ['fiction', 'adventure', 'history', 'science', 'romance']
BOOK_TARGET = 15000


def create_book(entry, source: str, idx: int):
    if source == "openlibrary":
        title = entry.get("title")
        author = entry.get("author_name", ["Unknown"])[0]
        published = entry.get("first_publish_name", random.randint(1900, 2020))
        pages = entry.get("number_of_pages_median", random.randint(100, 800))
        isbn = entry.get("isbn", [str(random.randint(10**12, 10**13 - 1))])[0]
    else:
        volume = entry.get("volumeInfo", {})
        title = volume.get("title")
        authors = volume.get("authors", ["Unknown"])
        author = authors[0]
        published = volume.get("publishedDate", "2000")[:4]
        pages = volume.get("pageCount", random.randint(100, 800))
        ids = volume.get("industryIdentifiers", [])
        isbn = ids[0]["identifier"] if ids else str(random.randint(10**12, 10**13 - 1))

    if not title or not author:
        return None
    
    key = f"{title.lower()}_{author.lower()}"
    uid = str(uuid.uuid5(uuid.NAMESPACE_DNS, key))

    return Book(
        book_id=idx,
        title=title,
        author=author,
        published_year=int(published) if str(published).isdigit() else 2000, category=random.choice(SUBJECTS),
        rating=round(random.uniform(1.0, 5.0), 2),
        availability=random.choice([True, False]),
        pages=pages,
        isbn=isbn,
        uuid=uid
    )
