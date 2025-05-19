import httpx


LL2_URL = "https://ll.thespacedevs.com/2.2.0/launch/?limit=100"


async def get_ll2_launches():
    async with httpx.AsyncClient() as client:
        response = await client.get(LL2_URL)
        response.raise_for_status()
        data = response.json()["results"]
        return [
            {
                "mission_name": l.get("name"),
                "launch_date": l.get("net"),
                "rocket_name": l.get("rocket", {}).get("configuration", {}).get("name"),
                "success": l.get("status", {}).get("name") == "Launch Successful",
                "agency": l.get("launch_service_provider", {}).get("name"),
                "details": l.get("mission", {}).get("description")
            }
            for l in data
        ]
    