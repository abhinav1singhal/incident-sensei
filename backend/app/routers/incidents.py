from fastapi import APIRouter
from app.services.incident_processor import processor
from typing import List
from app.models.incident import IncidentModel

router = APIRouter(prefix="/api/v1/incidents", tags=["incidents"])

@router.get("/", response_model=List[IncidentModel])
async def get_incidents():
    """Get all active incidents."""
    return processor.get_incidents()
