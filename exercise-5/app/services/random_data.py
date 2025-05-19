import httpx


async def fetch_random_users(batch: int = 1000):
    url = f"https://random-data-api.com/api/v2/users?size={batch}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()

        return response.json()
