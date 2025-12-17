import httpx
from app.config import settings
from typing import Dict, Any, List
import time

class DatadogService:
    def __init__(self):
        self.api_key = settings.DATADOG_API_KEY
        self.app_key = settings.DATADOG_APP_KEY
        # Handle case where DATADOG_SITE might be set to app.datadoghq.com in .env
        site = settings.DATADOG_SITE.replace("app.", "")
        self.base_url = f"https://api.{site}/api/v1"
        self.headers = {
            "DD-API-KEY": self.api_key,
            "DD-APPLICATION-KEY": self.app_key
        }

    async def get_metrics(self, query: str, from_time: int, to_time: int) -> Dict[str, Any]:
        """Query Datadog metrics."""
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                    f"{self.base_url}/query",
                    params={
                        "query": query,
                        "from": from_time,
                        "to": to_time
                    },
                    headers=self.headers
                )
                response.raise_for_status()
                return response.json()
            except Exception as e:
                print(f"Error fetching metrics: {e}")
                return {}

    async def get_logs(self, query: str, from_time: int, to_time: int) -> List[str]:
        """Fetch Logs (via List API - minimal version)."""
        # Note: Logs List API is v2 usually, but v1 exists for events.
        # Simplification: Mocking this part or using a simple endpoint if available.
        # For Hackathon, we might just mock if API is complex, but let's try a simple events query.
        async with httpx.AsyncClient() as client:
            try:
                # Using events API as proxy for logs/signals
                response = await client.get(
                    f"{self.base_url}/events",
                    params={
                        "start": from_time,
                        "end": to_time,
                        "tags": query 
                    },
                    headers=self.headers
                )
                if response.status_code == 200:
                    events = response.json().get("events", [])
                    return [e.get("text", "") for e in events[:5]] # Return top 5
                return []
            except Exception as e:
                print(f"Error fetching logs/events: {e}")
                return []

datadog_service = DatadogService()
