import httpx


OPEN_LIBRARY_URL = "https://openlibrary.org/search.json?q=subject:{}&limit=100"


async def fetch_openlibrary(subject: str, client: httpx.AsyncClient):
    url = OPEN_LIBRARY_URL.format(subject)
    try:
        resp = await client.get(url)
        return resp.json().get("docs", [])
    except:
        return []
