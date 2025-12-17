from pydantic import BaseModel
from typing import Optional, Dict, Any

class DatadogWebhookPayload(BaseModel):
    id: str
    event_type: str  # e.g., "metric_alert_monitor"
    title: str
    body: str
    alert_type: str # "error", "warning", "success", "info"
    date: int
    org: Optional[Dict[str, Any]] = None
    tags: Optional[str] = None # Datadog sends tags as CSV string usually
