import google.generativeai as genai
from app.config import settings
import json

class GeminiService:
    def __init__(self):
        if settings.GEMINI_API_KEY:
            genai.configure(api_key=settings.GEMINI_API_KEY)
            # User has access to 2.5 series
            self.model = genai.GenerativeModel('gemini-2.5-flash')
        else:
            print("[Gemini] No API Key configured.")
            self.model = None

    async def analyze_incident(self, context: dict) -> dict:
        if not self.model:
            return {
                "summary": "AI Analysis Unavailable (No Key)",
                "root_cause": "Unknown",
                "recommendations": []
            }

        prompt = f"""
        You are an Expert SRE. Analyze the following incident context and provide a structured JSON response.
        
        Incident: {context.get('title')}
        Severity: {context.get('severity')}
        
        Metrics: {context.get('metrics')}
        Logs: {context.get('logs')}
        Recent Events: {context.get('kafka_events')}
        
        Output format (JSON only):
        {{
            "summary": "One sentence summary for voice alert",
            "root_cause": "Likely root cause analysis",
            "recommendations": ["Action 1", "Action 2"]
        }}
        """
        
        try:
            response = await self.model.generate_content_async(prompt)
            # Simple cleanup for JSON parsing if model adds backticks
            text = response.text.replace('```json', '').replace('```', '')
            return json.loads(text)
        except Exception as e:
            print(f"[Gemini] Analysis failed: {e}")
            return {
                "summary": "Analysis failed due to error.",
                "root_cause": "Error",
                "recommendations": []
            }

gemini_service = GeminiService()
