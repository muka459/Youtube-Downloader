from pytube import YouTube
from pytube.cli import on_progress
import datetime

link = input("Enter youtube video link: ")

yt = YouTube(link, on_progress_callback=on_progress)

print("Title: " + yt.title)
print("Video length: " + str(datetime.timedelta(seconds=yt.length)) + "\n")

stream = yt.streams.filter(progressive=True)


for version in stream:
    print("Video ID: " + str(version.itag))
    print("MIME_type: " + version.mime_type)
    print("Resolution: " + version.resolution)
    print("FPS: " + str(version.fps))
    print("==============================")

id = input("Choose video id: ")

try:
    stream = yt.streams.get_by_itag(id)
    stream.download()
except:
    print("An unexpected error occurred")
    raise
