import requests
from app.config import settings

class TTSService:
    def __init__(self):
        self.api_key = settings.ELEVENLABS_API_KEY
        self.voice_id = "21m00Tcm4TlvDq8ikWAM" # Rachel (default)
        self.url = f"https://api.elevenlabs.io/v1/text-to-speech/{self.voice_id}"

    async def generate_audio(self, text: str) -> bytes:
        print(f"[TTS DEBUG] Key configured? {'Yes' if self.api_key else 'No'}")
        if not self.api_key:
            print("[TTS] No API Key, skipping audio.")
            return b""

        headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": self.api_key
        }

        data = {
            "text": text,
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.5
            }
        }

        try:
            # ElevenLabs generic API call (using synchronous requests here for simplicity, can be async'd)
            # In production, use httpx or run_in_executor
            print(f"[TTS DEBUG] Sending request to {self.url}")
            response = requests.post(self.url, json=data, headers=headers)
            print(f"[TTS DEBUG] Response Status: {response.status_code}")
            if response.status_code == 200:
                print(f"[TTS DEBUG] Received audio bytes: {len(response.content)}")
                return response.content
            else:
                print(f"[TTS] Error {response.status_code}: {response.text}")
                return b""
        except Exception as e:
            print(f"[TTS] Generation failed: {e}")
            import traceback
            traceback.print_exc()
            return b""

tts_service = TTSService()
