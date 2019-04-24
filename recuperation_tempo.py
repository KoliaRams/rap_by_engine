import librosa
import youtube_dl

prod_audio = input("Entrer un url d'une prod youtube : ")

opts = {
    'format': 'bestaudio/best',
    'outtmpl': '/home/mars/Bureau/tweetstrump/son',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
    }],

}
with youtube_dl.YoutubeDL(opts) as ydl:
    ydl.download([prod_audio])

y, sr = librosa.load('wav')

tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

print('tempo {:.2f} beats'.format(tempo))
