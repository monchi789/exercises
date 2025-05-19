from fastapi import APIRouter
from .services.analysis import get_combined_launch_analysis
from .models.schema import LaunchResponse

router = APIRouter()

@router.get("/launches/analyze", response_model=LaunchResponse)
async def analyze_launches():
    return await get_combined_launch_analysis()