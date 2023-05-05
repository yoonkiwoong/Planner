from typing import List

from fastapi import APIRouter, HTTPException, status, Body
from models.events import Event

event_router = APIRouter(
    tags=["Events"]
)

events = []

@event_router.get("/", response_model=Event)
async def retrieve_all_events() -> List[Event]:
    return events

@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: int) -> Event:
    for event in events:
        if event.id == id:
            return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )

@event_router.post("/new")
async def create_event(body: Event = Body(...)) -> dict:
    events.append(body)
    return{
        "Message": "Event created successfully"
    }

@event_router.delete("/")
async def delete_all_events() -> dict:
    events.clear()
    return{
        "message": "Events deleted successfully"
    }

@event_router.delete("/{id}")
async def delete_event(id: int) -> dict:
    for event in events:
        if event.id == id:
            event.remove(event)
            return{
                "Message": "Event deleted successfully"
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )