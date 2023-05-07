import httpx
import pytest

from models.events import Event

@pytest.fixture(scope="module")
async def mock_event() -> Event:
    new_event = Event(
        creator="sampleuser@sample.com",
        title="FastAPI",
        image="FastAPI.png",
        description="This is my FastAPI Sample App",
        tags=["python", "fastapi"],
        location="Google Meet"
    )

    await Event.insert_one(new_event)

    yield new_event

@pytest.mark.asyncio
async def test_get_events(default_client: httpx.AsyncClient, mock_event: Event) -> None:
    response = await default_client.get("/event/")

    assert response.status_code == 200
    assert response