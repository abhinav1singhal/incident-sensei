from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    APP_NAME: str = "Incident Sensei"
    
    # Datadog
    DATADOG_API_KEY: str
    DATADOG_APP_KEY: str
    DATADOG_SITE: str = "datadoghq.com"
    
    # Confluent Kafka
    CONFLUENT_BOOTSTRAP_SERVERS: str
    CONFLUENT_API_KEY: str
    CONFLUENT_API_SECRET: str
    
    # AI & Voice
    GEMINI_API_KEY: str
    ELEVENLABS_API_KEY: str
    
    # Security
    WEBHOOK_SECRET: str

    class Config:
        env_file = ".env"
        extra = "ignore"  # Ignore other env vars

settings = Settings()
