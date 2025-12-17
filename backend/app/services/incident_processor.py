from app.models.incident import IncidentModel
from app.models.webhook import DatadogWebhookPayload
from app.services.datadog_service import datadog_service
from app.services.kafka_service import kafka_service
from app.services.gemini_service import gemini_service
from app.services.tts_service import tts_service
import datetime
import uuid
import os
import time

class IncidentProcessor:
    def __init__(self):
        self.incidents: list[IncidentModel] = []

    def get_incidents(self) -> list[IncidentModel]:
        return sorted(self.incidents, key=lambda x: x.created_at, reverse=True)

    async def process_webhook(self, payload: DatadogWebhookPayload) -> IncidentModel:
        """
        Orchestrates the incident processing pipeline.
        """
        start_time = time.time()
        incident_id = str(uuid.uuid4())
        print(f"[Processor:{incident_id}] Starting processing for: {payload.title}")

        # 1. Gather Context (Parallel execution would be better, doing serial for simplicity)
        # Fetch mock signals for hackathon if no real data
        now = int(time.time())
        metrics = await datadog_service.get_metrics("system.cpu.idle", now - 300, now)
        logs = await datadog_service.get_logs("source:my-service", now - 300, now)
        events = kafka_service.get_recent_events(limit=5)

        context = {
            "title": payload.title,
            "severity": payload.alert_type,
            "metrics": metrics,
            "logs": logs,
            "kafka_events": events
        }

        # 2. AI Analysis
        analysis = await gemini_service.analyze_incident(context)
        
        # 3. Voice Generation
        voice_summary = analysis.get("summary", f"Alert: {payload.title}. Check dashboard.")
        audio_content = await tts_service.generate_audio(voice_summary)
        
        audio_url = None
        if audio_content:
            filename = f"{incident_id}.mp3"
            filepath = f"app/static/audio/{filename}"
            with open(filepath, "wb") as f:
                f.write(audio_content)
            # Assuming backend runs on port 8000
            # In production, use standard base URL
            audio_url = f"http://localhost:8000/static/audio/{filename}"

        # 4. Construct Incident
        incident = IncidentModel(
            id=incident_id,
            title=payload.title,
            severity="critical" if "error" in payload.alert_type else "warning",
            status="active",
            created_at=datetime.datetime.now().isoformat(),
            summary=voice_summary,
            root_cause=analysis.get("root_cause"),
            audio_url=audio_url,
            metrics={"cpu": 99.9}, # Simplification for UI
            logs=context.get("logs", []),
            kafka_events=context.get("kafka_events", [])
        )

        print(f"[Processor:{incident_id}] Completed in {time.time() - start_time:.2f}s")
        self.incidents.append(incident)
        return incident

processor = IncidentProcessor()
