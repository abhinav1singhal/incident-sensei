export interface Incident {
    id: string;
    title: string;
    severity: string; // 'critical' | 'error' | 'warning' | 'info'
    status: string;
    created_at: string;
    summary?: string;
    root_cause?: string;
    audio_url?: string;
    metrics?: Record<string, any>;
    logs?: string[];
    kafka_events?: any[];
}

export interface WebhookPayload {
    id: string;
    event_type: string;
    title: string;
    body: string;
    alert_type: string;
    date: number;
}
