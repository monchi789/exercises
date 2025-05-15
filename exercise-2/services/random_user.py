import httpx
import asyncio

async def get_random_names(count: int = 100):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://randomuser.me/api/?results={count}")
        response.raise_for_status()
        data = response.json()

        return [
            {
                "first_name": user["name"]["first"],
                "last_name": user["name"]["last"]
            }
            for user in data["results"]
        ]

async def get_all_names(total: int = 1500, batch_size: int = 100):
    all_names = []
    for _ in range(total // batch_size):
        batch = await get_random_names(batch_size)
        all_names.extend(batch)
        await asyncio.sleep(1.1)  # espera para evitar el 429
    return all_names