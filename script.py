import yt_dlp

user_input = input("Fügen Sie Ihren Youtube Link ein: ")

ydl_opts = {
    "format": "bestvideo[vcodec^=avc1][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
    "outtmpl": "/Users/konstantin/Documents/Videos/%(title)s.%(ext)s",
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(user_input)
    print("Download erfolgreich!")

