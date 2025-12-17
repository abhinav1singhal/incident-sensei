import React, { } from 'react';

interface Props {
    audioRef: React.RefObject<HTMLAudioElement>;
}

export function AudioPlayer({ audioRef }: Props) {
    return (
        <div className="audio-player-container">
            <audio ref={audioRef} controls style={{ display: 'none' }} />
            <div className="player-indicator">
                🔊 Voice Alerts Active
            </div>
        </div>
    );
}
