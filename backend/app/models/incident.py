from pydantic import BaseModel
from typing import Dict, Any, Optional

class IncidentModel(BaseModel):
    id: str
    title: str
    severity: str  # critical, error, warning, info
    status: str    # active, resolved
    summary: Optional[str] = None
    root_cause: Optional[str] = None
    audio_url: Optional[str] = None
    created_at: str
    
    # Context
    metrics: Dict[str, Any] = {}
    logs: list[str] = []
    kafka_events: list[Dict[str, Any]] = []
