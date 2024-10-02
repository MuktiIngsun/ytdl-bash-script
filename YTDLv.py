from pytube import YouTube

url = input("YT Link: ")
yt = YouTube(url)

print("Judul: ", yt.title)
print("""1\) 360p
2\) 480p
3\) 720p""")
resolusi = str(input("Pilih Resolusi (1/2/3): "))

if resolusi == '1':
    print("Sedang Download")
    video = yt.streams.get_by_itag(18)
    video.download()
elif resolusi == '2':
    print("Sedang Download")
    video = yt.streams.get_by_itag(135)
    video.download(filename_prefix="TEMP ")
    audio = yt.streams.get_by_itag(251)
    audio.download()
elif resolusi == '3':
    print("Sedang Download")
    video = yt.streams.get_by_itag(136)
    video.download(filename_prefix="TEMP ")
    audio = yt.streams.get_by_itag(251)
    audio.download()