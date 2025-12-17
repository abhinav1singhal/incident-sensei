import { useIncidents } from './hooks/useIncidents';
import { IncidentList } from './components/IncidentList';
import { AudioPlayer } from './components/AudioPlayer';
import './styles/index.css';

function App() {
    const { incidents, loading, error, audioRef } = useIncidents();

    return (
        <div className="app-container">
            <header className="app-header">
                <div className="logo">
                    🥋 <span>Incident Sensei</span>
                </div>
                <div className="status-bar">
                    <span className={`status-dot ${error ? 'error' : 'live'}`}></span>
                    {error ? 'Connection Error' : 'System Operational'}
                </div>
            </header>

            <main>
                <div className="dashboard-content">
                    <div className="hero-section">
                        <h1>Real-Time Incident Intelligence</h1>
                        <p className="subtitle">Voice-enabled SRE monitoring powered by Gemini & Datadog</p>
                    </div>

                    <AudioPlayer audioRef={audioRef} />

                    {loading ? (
                        <div className="loading">Initializing Neural Link...</div>
                    ) : (
                        <IncidentList incidents={incidents} />
                    )}

                    {error && <div className="error-banner">{error}</div>}
                </div>
            </main>

            <div className="background-gradient"></div>
        </div>
    );
}

export default App;
