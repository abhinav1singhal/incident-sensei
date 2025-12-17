# 🥋 Incident Sensei

> **Real-time, Voice-Enabled Incident Detection & Analysis Platform**

Incident Sensei is an intelligent incident management system that combines Datadog monitoring, Confluent Kafka event streaming, Google Gemini AI analysis, and ElevenLabs voice synthesis to provide SRE teams with instant, spoken incident summaries.

---

## 🎯 Features

- **🚨 Real-Time Detection**: Automated incident alerting via Datadog webhooks
- **🔗 Signal Correlation**: Combines metrics, logs, and Kafka events for context
- **🧠 AI Analysis**: Gemini-powered root cause analysis and recommendations
- **🗣️ Voice Alerts**: Natural speech incident summaries via ElevenLabs
- **📊 Live Dashboard**: Real-time incident updates with audio playback

---

## 🏗️ Architecture

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Datadog   │───▶│   Backend   │◀──▶│   Gemini    │
│  (Webhooks) │    │  (FastAPI)  │    │    (AI)     │
└─────────────┘    └──────┬──────┘    └─────────────┘
                          │
┌─────────────┐           │           ┌─────────────┐
│   Kafka     │◀──────────┤           │ ElevenLabs  │
│  (Events)   │           │           │   (TTS)     │
└─────────────┘           ▼           └─────────────┘
                   ┌─────────────┐
                   │  Frontend   │
                   │  (React)    │
                   └─────────────┘
```

See [architecture.md](./architecture.md) for detailed system design.

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Node.js 18+
- Docker (optional)
- API Keys for: Datadog, Confluent, Gemini, ElevenLabs

### Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your API keys

# Run development server
uvicorn app.main:app --reload --port 8000
```

### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Configure environment
cp .env.example .env
# Edit .env with backend URL

# Run development server
npm run dev
```

---

## 📁 Project Structure

```
incident-sensei/
├── backend/
│   ├── app/
│   │   ├── main.py           # FastAPI entry point
│   │   ├── config.py         # Configuration
│   │   ├── models/           # Data models
│   │   ├── routers/          # API endpoints
│   │   ├── services/         # Business logic
│   │   └── utils/            # Helpers
│   ├── tests/                # Unit tests
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── components/       # React components
│   │   ├── hooks/            # Custom hooks
│   │   ├── services/         # API client
│   │   └── types/            # TypeScript types
│   ├── package.json
│   └── vite.config.ts
├── architecture.md           # System design doc
└── README.md
```

---

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `DATADOG_API_KEY` | Datadog API key | ✅ |
| `DATADOG_APP_KEY` | Datadog App key | ✅ |
| `CONFLUENT_BOOTSTRAP_SERVERS` | Kafka servers | ✅ |
| `CONFLUENT_API_KEY` | Confluent Cloud key | ✅ |
| `CONFLUENT_API_SECRET` | Confluent Cloud secret | ✅ |
| `GEMINI_API_KEY` | Google AI API key | ✅ |
| `ELEVENLABS_API_KEY` | ElevenLabs API key | ✅ |
| `WEBHOOK_SECRET` | Webhook signature secret | ✅ |

---

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest tests/ -v
```

### Frontend Tests
```bash
cd frontend
npm test
```

---

## 🚢 Deployment

### Google Cloud Run

```bash
# Build and deploy backend
cd backend
gcloud run deploy incident-sensei-backend \
  --source . \
  --region us-central1 \
  --allow-unauthenticated

# Deploy frontend to Cloud Storage or preferred CDN
```

---

## 🎬 Demo Script

1. **Show Dashboard** — Healthy state, no active incidents
2. **Trigger Incident** — Simulate or trigger real Datadog alert
3. **Watch Processing** — Backend correlates data, generates analysis
4. **Hear Voice Alert** — ElevenLabs reads incident summary
5. **See Dashboard Update** — Real-time incident card appears

---

## 📋 Implementation Roadmap

### Phase 1: Foundation (Day 1)
- [ ] Set up project structure
- [ ] Backend skeleton with FastAPI
- [ ] Frontend skeleton with React + Vite
- [ ] Health check endpoints

### Phase 2: Core Integrations (Day 1-2)
- [ ] Datadog webhook handler
- [ ] Datadog Metrics/Logs API client
- [ ] Kafka consumer setup
- [ ] Basic incident processing pipeline

### Phase 3: AI & Voice (Day 2)
- [ ] Gemini prompt engineering
- [ ] Analysis response parsing
- [ ] ElevenLabs TTS integration
- [ ] Audio file serving

### Phase 4: Frontend (Day 2-3)
- [ ] Incident list component
- [ ] Incident detail view
- [ ] Audio player integration
- [ ] SSE real-time updates

### Phase 5: Polish & Demo (Day 3)
- [ ] Error handling & fallbacks
- [ ] UI polish & dark theme
- [ ] Demo script preparation
- [ ] Deployment to Cloud Run

---

## 🛡️ Security

- Webhook payload signature verification
- API keys stored in GCP Secret Manager
- HTTPS-only communication
- CORS restricted to known origins

---

## 📊 Success Metrics

| Metric | Target |
|--------|--------|
| Incident processing time | < 5 seconds |
| Audio generation time | < 3 seconds |
| Demo stability | 100% |
| Signal correlation accuracy | Visible to judges |

---

## 🏆 Hackathon Sponsors

- **Datadog** — Monitoring & Observability
- **Confluent** — Real-time Event Streaming
- **Google Cloud** — AI (Gemini) & Infrastructure
- **ElevenLabs** — Voice Synthesis

---

## 📄 License

MIT License — See [LICENSE](./LICENSE) for details.

---

## 👥 Team

Built with ❤️ for the hackathon.
