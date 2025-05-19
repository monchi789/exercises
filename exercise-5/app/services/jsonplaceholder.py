import httpx


async def fetch_jsonplaceholder_users():
    url = "https://jsonplaceholder.typicode.com/users"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        
        return response.json()