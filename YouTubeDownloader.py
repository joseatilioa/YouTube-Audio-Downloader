from pytube import YouTube

while True:
    link = input('Enter YouTube link: ')
    yt = YouTube(link)
    print('Titulo: ', yt.title)
    yt.streams.filter(only_audio=True)
    ys = yt.streams.get_by_itag(251)
    print('Downloading...')
    ys.download('Music')
    print('Download completed')
    continue
