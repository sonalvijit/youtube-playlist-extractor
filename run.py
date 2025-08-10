import yt_dlp

playlist_url = "https://www.youtube.com/playlist?list=PLnlL14v8ZEzc-MMJ6wLj-Xr7Xx8lKzYRx"

ydl_opts = {
    'extract_flat': True,  # Don't download, just extract info
    'quiet': True,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    playlist_dict = ydl.extract_info(playlist_url, download=False)

    print(f"Playlist Title: {playlist_dict.get('title')}")
    print(f"Total videos: {len(playlist_dict.get('entries', []))}\n")

    for video in playlist_dict.get('entries', []):
        print(f"https://www.youtube.com/watch?v={video['id']}")
