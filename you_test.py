import youtube_dl

opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav'
    }],
}

with youtube_dl.YoutubeDL(opts) as ydl:
    ydl.download(["https://www.youtube.com/watch?v=_0JhZ7B5-Aw"])