from pytube import YouTube

while True:
    link = input('Introduce el link de YouTube: ')
    try:
        yt = YouTube(link)
        yt = str
    except:
        print('Link no valido')
        continue

    print('Titulo: ', yt.title)
    yt.streams.filter(only_audio=True)
    ys = yt.streams.get_by_itag(251)
    print('Descargando...')
    ys.download('Desktop')
    print('Descarga finalizada')
    continue
