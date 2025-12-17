import { useState, useEffect, useRef } from 'react';
import { api } from '../services/api';
import { Incident } from '../types';

export function useIncidents() {
    const [incidents, setIncidents] = useState<Incident[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);
    const audioRef = useRef<HTMLAudioElement | null>(null);
    const lastPlayedIdRef = useRef<string | null>(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const data = await api.getIncidents();
                setIncidents(data);

                // Auto-play latest audio if new
                if (data.length > 0) {
                    const latest = data[0];
                    if (latest.audio_url && latest.id !== lastPlayedIdRef.current) {
                        console.log("New incident with audio, playing...", latest.title);
                        lastPlayedIdRef.current = latest.id;
                        if (audioRef.current) {
                            audioRef.current.src = api.getAudioUrl(latest.audio_url);
                            audioRef.current.play().catch(e => console.error("Auto-play blocked", e));
                        }
                    }
                }

                setError(null);
            } catch (err: any) {
                console.error(err);
                setError(err.message);
            } finally {
                setLoading(false);
            }
        };

        fetchData();
        const interval = setInterval(fetchData, 2000); // Poll every 2s

        return () => clearInterval(interval);
    }, []);

    return { incidents, loading, error, audioRef };
}
