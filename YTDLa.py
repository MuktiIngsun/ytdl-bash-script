from pytube import YouTube

url = input("YT Link: ")
yt = YouTube(url)

print("Judul: ", yt.title)
print("Sedang Download")
audio = yt.streams.get_by_itag(251)
audio.download()
