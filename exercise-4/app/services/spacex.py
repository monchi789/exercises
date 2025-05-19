import httpx


SPACEX_URL = "https://api.spacexdata.com/v4/launches"


async def get_spacex_launches(limit=100):
    async with httpx.AsyncClient() as client:
        response = await client.get(SPACEX_URL)
        response.raise_for_status()
        data = response.json()
        launches = sorted(data, key=lambda x: x["date_utc"], reverse=True)

        return [
            {
                "mission_name": l["name"],
                "launch_date": l["date_utc"],
                "rocket_name": l.get("rocket", "Unknown"),
                "success": l.get("success"),
                "agency": "SpaceX",
                "details": l.get("details")
            }

            for l in launches[:limit]
        ]