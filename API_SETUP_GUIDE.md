# Incident Sensei — API Setup Guide

This guide walks you through obtaining API keys for all required services.

---

## 1. Google Gemini API (AI Analysis)

**Free tier available** ✅

### Steps:
1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account
3. Click **"Get API Key"** in the left sidebar
4. Click **"Create API Key"**
5. Copy and save your API key

### Environment Variable:
```
GEMINI_API_KEY=your_api_key_here
```

> **Tip**: Gemini 1.5 Flash has generous free limits (1500 requests/day)

---

## 2. ElevenLabs API (Voice Synthesis)

**Free tier available** ✅ (10,000 characters/month)

### Steps:
1. Go to [ElevenLabs](https://elevenlabs.io/)
2. Click **"Sign Up"** and create an account
3. After logging in, click your profile icon (top right) → **"Profile + API Key"**.
4. Click the "eye" icon to reveal and copy your API Key.

**Note:** This single API key grants access to all services, including the **Text-to-Speech** customization we will use. You do not need to create a specific "project" key.

### Environment Variable:
```
ELEVENLABS_API_KEY=your_api_key_here
```

> **Tip**: The free tier is enough for hackathon demos

---

## 3. Datadog API (Monitoring & Webhooks)

**14-day free trial** ✅

### Steps:
1. Go to [Datadog](https://www.datadoghq.com/)
2. Click **"Get Started Free"**
3. Create an account and complete onboarding
4. Navigate to **Organization Settings** → **API Keys**
5. Click **"New Key"** to create an API key
6. Navigate to **Organization Settings** → **Application Keys**
7. Click **"New Key"** to create an App key

### Environment Variables:
```
DATADOG_API_KEY=your_api_key_here
DATADOG_APP_KEY=your_app_key_here
DATADOG_SITE=datadoghq.com
```

### Setting up Webhooks:
1. Go to **Integrations** → **Webhooks**
2. Click **"New Webhook"**
3. Set URL to your backend endpoint: `https://your-backend.run.app/api/v1/webhook/datadog`
4. (For local testing, use ngrok: `ngrok http 8000`)

---

## 4. Confluent Cloud (Kafka Streaming)

**Free tier available** ✅ ($400 credit for new accounts)

### Steps:
1. Go to [Confluent Cloud](https://confluent.cloud/)
2. Click **"Start Free"** and create an account
3. Create a new **Basic cluster** (free tier eligible)
4. Once created, go to **API Keys** in your cluster
5. Click **"Create Key"** → Choose "Global Access" for hackathon

### Create Topic:
1. Go to **Topics** in your cluster
2. Click **"Create Topic"**
3. Name it: `incident-events`
4. Keep default settings

### Environment Variables:
```
CONFLUENT_BOOTSTRAP_SERVERS=pkc-xxxxx.us-east1.gcp.confluent.cloud:9092
CONFLUENT_API_KEY=your_cluster_api_key
CONFLUENT_API_SECRET=your_cluster_api_secret
```

---

## 5. Google Cloud (Deployment)

**$300 free credit for new accounts** ✅

### Steps:
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project named `incident-sensei`
3. Enable the **Cloud Run API**
4. Install [gcloud CLI](https://cloud.google.com/sdk/docs/install)

### Authenticate:
```bash
gcloud auth login
gcloud config set project incident-sensei
```

---

## Quick Reference: All Environment Variables

Create a `.env` file in your backend folder:

```bash
# Google Gemini
GEMINI_API_KEY=

# ElevenLabs
ELEVENLABS_API_KEY=

# Datadog
DATADOG_API_KEY=
DATADOG_APP_KEY=
DATADOG_SITE=datadoghq.com

# Confluent Kafka
CONFLUENT_BOOTSTRAP_SERVERS=
CONFLUENT_API_KEY=
CONFLUENT_API_SECRET=

# Webhook Security (generate a random string)
WEBHOOK_SECRET=your_random_secret_string
```

---

## Recommended Setup Order

| Priority | Service | Time to Setup | Reason |
|----------|---------|---------------|--------|
| 1 | **Gemini** | 2 min | Instant, core AI feature |
| 2 | **ElevenLabs** | 2 min | Instant, voice feature |
| 3 | **Datadog** | 10 min | Trial signup, main integration |
| 4 | **Confluent** | 10 min | Cluster creation takes time |
| 5 | **Google Cloud** | 15 min | For deployment (can do later) |

---

## Alternative: Mock Mode

If you want to start coding before getting all API keys, I can implement a **mock mode** that:
- Simulates Datadog webhooks
- Uses fake metrics/logs data
- Returns placeholder AI analysis
- Uses browser TTS instead of ElevenLabs

This lets you build and demo the UI immediately!

---

## Need Help?

Let me know which service you'd like to set up first, and I can provide more detailed guidance or help troubleshoot any issues.
