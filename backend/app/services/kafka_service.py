from confluent_kafka import Consumer, KafkaException
from app.config import settings
import threading
import json
from collections import deque
import time

class KafkaService:
    def __init__(self):
        self.running = False
        self.buffer = deque(maxlen=50) # Keep last 50 events
        self.thread = None
        
        self.conf = {
            'bootstrap.servers': settings.CONFLUENT_BOOTSTRAP_SERVERS,
            'security.protocol': 'SASL_SSL',
            'sasl.mechanisms': 'PLAIN',
            'sasl.username': settings.CONFLUENT_API_KEY,
            'sasl.password': settings.CONFLUENT_API_SECRET,
            'group.id': 'incident-sensei-backend-1',
            'auto.offset.reset': 'latest'
        }

    def start(self):
        """Start background consumer thread."""
        if not settings.CONFLUENT_BOOTSTRAP_SERVERS:
            print("[Kafka] No bootstrap servers configured, skipping.")
            return

        self.running = True
        self.thread = threading.Thread(target=self._consume_loop, daemon=True)
        self.thread.start()
        print("[Kafka] Consumer started.")

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join(timeout=1.0)

    def _consume_loop(self):
        try:
            consumer = Consumer(self.conf)
            consumer.subscribe(['incident-events'])

            while self.running:
                msg = consumer.poll(1.0)
                if msg is None:
                    continue
                if msg.error():
                    print(f"[Kafka] Error: {msg.error()}")
                    continue

                try:
                    value = msg.value().decode('utf-8')
                    event = json.loads(value)
                    # Add timestamp if missing
                    if 'timestamp' not in event:
                        event['timestamp'] = time.time()
                    self.buffer.append(event)
                    # print(f"[Kafka] Consumed: {event}")
                except Exception as e:
                    print(f"[Kafka] Parse error: {e}")

            consumer.close()
        except Exception as e:
            print(f"[Kafka] Connection error: {e}")

    def get_recent_events(self, limit: int = 10) -> list:
        return list(self.buffer)[-limit:]

kafka_service = KafkaService()
