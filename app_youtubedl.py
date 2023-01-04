# Importar la biblioteca os
import os

# URL de la canción de YouTube Music que quieres descargar
url = "https://www.youtube.com/watch?v=1-xGerv5FOk"

# Ejecutar youtube-dl para descargar la canción
os.system("youtube-dl -f bestaudio " + url)
