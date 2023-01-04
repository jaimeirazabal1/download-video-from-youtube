# Importar la biblioteca pytube
import pytube

# URL de la lista de reproducción de YouTube Music
url = "https://www.youtube.com/watch?v=2jYEz66J_J4&list=RDQMChKP9mHrww0&start_radio=1"

# Obtener la lista de reproducción de YouTube
yt = pytube.Playlist(url)

# Recorrer la lista de canciones y descargarlas
if len(yt) == 0:
    print('No se encontro musica en este link ',url)
else:
    for song in yt:
        print("Descargando canción: " + song.title)
        song.download()

    print("¡Descarga completa!")
