import pytest
import httpx
from app.services.spacex import get_spacex_launches

@pytest.mark.asyncio
async def test_get_spacex_launches(monkeypatch):
    mock_data = [
        {
            "name": "FalconSat",
            "date_utc": "2006-03-24T22:30:00.000Z",
            "rocket": "Falcon 1",
            "success": False,
            "details": "Engine failure at 33 seconds and loss of vehicle"
        }
    ]

    async def mock_get(*args, **kwargs):
        class MockResponse:
            def raise_for_status(self): pass
            def json(self): return mock_data
        return MockResponse()

    class MockAsyncClient:
        async def __aenter__(self): return self
        async def __aexit__(self, exc_type, exc, tb): pass
        async def get(self, *args, **kwargs): return await mock_get()

    monkeypatch.setattr(httpx, "AsyncClient", MockAsyncClient)

    launches = await get_spacex_launches(limit=1)
    assert len(launches) == 1
    assert launches[0]["mission_name"] == "FalconSat"
    assert launches[0]["rocket_name"] == "Falcon 1"
    assert launches[0]["success"] is False
    assert launches[0]["agency"] == "SpaceX"
    assert launches[0]["details"] == "Engine failure at 33 seconds and loss of vehicle"