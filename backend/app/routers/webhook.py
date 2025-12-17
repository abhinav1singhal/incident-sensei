from fastapi import APIRouter, HTTPException, Request, Header
from app.models.webhook import DatadogWebhookPayload
from app.services.incident_processor import processor
from app.config import settings

router = APIRouter(prefix="/api/v1/webhook", tags=["webhooks"])

@router.post("/datadog")
async def handle_datadog_webhook(
    payload: DatadogWebhookPayload,
    # x_datadog_signature: str = Header(None) # TODO: Add signature verification
):
    """
    Receives alerts from Datadog and triggers the incident pipeline.
    """
    try:
        incident = await processor.process_webhook(payload)
        return {"status": "accepted", "incident_id": incident.id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
