import librosa

y, sr = librosa.load('exemple.wav')

tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

print('tempo {:.2f} beats'.format(tempo))
