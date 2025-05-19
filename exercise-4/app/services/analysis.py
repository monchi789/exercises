from collections import Counter, defaultdict
from .spacex import get_spacex_launches
from .launch_library import get_ll2_launches
from ..utils.cache import cached_response


@cached_response(ttl=60)
async def get_combined_launch_analysis():
    spacex, ll2 = await get_spacex_launches(), await get_ll2_launches()
    combined = spacex + ll2

    # Statistics
    total = len(combined)
    successes = sum(1 for l in combined if l["success"])
    launches_by_year = defaultdict(int)
    agency_counter = Counter()
    rocket_counter = Counter()

    for launch in combined:
        year = launch["launch_date"][:4]
        launches_by_year[year] += 1
        agency_counter[launch["agency"]] += 1
        rocket_counter[launch["rocket_name"]] += 1

    
    return {
        "launches": combined,
        "statistics": {
            "success_rate": round(successes / total * 100, 2),
            "launches_by_year": dict(launches_by_year),
            "top_agencies": agency_counter.most_common(5),
            "most_used_rockets": rocket_counter.most_common(5)
        }
    }