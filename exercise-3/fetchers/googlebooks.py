import httpx


GOOGLEBOOKS_URL = "https://www.googleapis.com/books/v1/volumes?q=subject:{}&maxResults=40"


async def fetch_googlebooks(subject: str, client: httpx.AsyncClient):
    url = GOOGLEBOOKS_URL.format(subject)
    try:
        resp = await client.get(url)
        return resp.json().get("items", [])
    except:
        return []
