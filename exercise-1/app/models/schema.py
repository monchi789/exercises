from pydantic import BaseModel
from typing import List, Optional, Dict, Tuple


class Launch(BaseModel):
    mission_name: str
    launch_date: str
    rocket_name: Optional[str]
    success: Optional[bool]
    agency: str
    details: Optional[str]


class Statistics(BaseModel):
    success_rate: float
    launches_by_year: Dict[str, int]
    top_agencies: List[Tuple[str, int]]
    most_used_rockets: List[Tuple[str, int]]


class LaunchResponse(BaseModel):
    launches: List[Launch]
    statistics: Statistics
