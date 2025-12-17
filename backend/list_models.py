import google.generativeai as genai
from app.config import settings
import os

# Force load env vars if not loaded by ensuring script runs in correct context or manually loading
# But since we import settings, it should load from .env if we run from backend working dir

def list_models():
    if not settings.GEMINI_API_KEY:
        print("Error: GEMINI_API_KEY not found in settings.")
        return

    genai.configure(api_key=settings.GEMINI_API_KEY)

    print("Listing available models...")
    try:
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(f"- {m.name}")
    except Exception as e:
        print(f"Error listing models: {e}")

if __name__ == "__main__":
    list_models()
