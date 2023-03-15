from pytube import YouTube
from sys import argv

# extracting second command from command line
link = argv[1]
yt = YouTube(link)

print("Title: " + yt.title + "\n Author: " + yt.author)

vd = yt.streams.get_highest_resolution()

vd.download('D:\Python\Projects\VideoDownloader')
