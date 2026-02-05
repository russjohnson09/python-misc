import datetime

#  uv run ./tests/youtube_download.py 
# <module 'datetime' from 'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.13_3.13.2544.0_x64__qbz5n2kfra8p0\\Lib\\datetime.py'>
print(datetime)



print(datetime.datetime)




# from pytube import YouTube
# from pytube import YouTube

# print("download")
# # YouTube('https://youtu.be/2lAe1cqCOXo').streams.first().download()
# #   File "C:\Users\russj\dev\python-misc\pygame\galaga\.venv\Lib\site-packages\pytube\__main__.py", line 296, in streams
#     # return StreamQuery(self.fmt_streams)
# YouTube('https://www.youtube.com/watch?v=7s7Ld0XUbVQ').streams.first().download()

#  yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
#  yt.streams
# .filter(progressive=True, file_extension='mp4')
# .order_by('resolution')
# .desc()
#   ... .first()
#   ... .download()


from yt_dlp import YoutubeDL

print("test")
URLS = ['https://www.youtube.com/watch?v=7s7Ld0XUbVQ']
# [youtube] Extracting URL: https://www.youtube.com/watch?v=7s7Ld0XUbVQ 
# [youtube] 7s7Ld0XUbVQ: Downloading webpage 
# WARNING: [youtube] No supported JavaScript runtime could be found. Only deno is enabled by default; to use another runtime add  --js-runtimes RUNTIME[:PATH]  to your command/config. YouTube extraction without a JS runtime has been deprecated, and some formats may be missing. See  https://github.com/yt-dlp/yt-dlp/wiki/EJS  for details on installing one
# [youtube] 7s7Ld0XUbVQ: Downloading android vr player API JSON 
# WARNING: ffmpeg not found. The downloaded format may not be the best available. Installing ffmpeg is strongly recommended: https://github.com/yt-dlp/yt-dlp#dependencies 
# [info] 7s7Ld0XUbVQ: Downloading 1 format(s): 18 
# [download] Destination: We're Straight Up Cafe Cozy-Maxing in TAILSIDE： COZY CAFE SIM [7s7Ld0XUbVQ].mp4 
# [download] 100% of  313.90MiB in 00:00:21 at 14.87MiB/s
with YoutubeDL() as ydl:
    ydl.download(URLS)