import httpx


async def fetch_random_users():
    url = "https://randomuser.me/api/?results=1500"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()

        data = response.json()

        return data["results"]