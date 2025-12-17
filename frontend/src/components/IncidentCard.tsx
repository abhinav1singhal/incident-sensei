import { Incident } from '../types';

interface Props {
    incident: Incident;
    isActive: boolean;
}

export function IncidentCard({ incident, isActive }: Props) {
    return (
        <div className={`incident-card ${isActive ? 'active' : ''} ${incident.severity}`}>
            <div className="card-header">
                <span className={`badge ${incident.severity}`}>{incident.severity.toUpperCase()}</span>
                <span className="timestamp">{new Date(incident.created_at).toLocaleTimeString()}</span>
            </div>

            <h3>{incident.title}</h3>

            <p className="summary">{incident.summary}</p>

            {incident.root_cause && (
                <div className="analysis-box">
                    <strong>🤖 AI Analysis:</strong>
                    <p>{incident.root_cause}</p>
                </div>
            )}

            <div className="metrics-row">
                {incident.metrics && Object.entries(incident.metrics).map(([key, val]) => (
                    <div key={key} className="metric">
                        <span className="label">{key}:</span>
                        <span className="value">{val}</span>
                    </div>
                ))}
            </div>
        </div>
    );
}
