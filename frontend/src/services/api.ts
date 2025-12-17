import { Incident } from '../types';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export const api = {
    async getIncidents(): Promise<Incident[]> {
        const response = await fetch(`${API_URL}/api/v1/incidents/`);
        if (!response.ok) {
            throw new Error('Failed to fetch incidents');
        }
        return response.json();
    },

    getAudioUrl(path: string): string {
        if (path.startsWith('http')) return path;
        return `${API_URL}/${path}`;
    }
};
