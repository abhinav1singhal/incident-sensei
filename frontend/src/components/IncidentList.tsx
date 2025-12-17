import { Incident } from '../types';
import { IncidentCard } from './IncidentCard';

interface Props {
    incidents: Incident[];
}

export function IncidentList({ incidents }: Props) {
    if (incidents.length === 0) {
        return (
            <div className="empty-state">
                <h2>No Active Incidents</h2>
                <p>System is healthy. Monitoring signals...</p>
                <div className="pulse-ring"></div>
            </div>
        );
    }

    return (
        <div className="incident-list">
            {incidents.map((incident, index) => (
                <IncidentCard
                    key={incident.id}
                    incident={incident}
                    isActive={index === 0}
                />
            ))}
        </div>
    );
}
