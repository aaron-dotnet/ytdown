from pytubefix import YouTube
from pytubefix.cli import on_progress

"""
Notas:
Esta parte viene de la documentacion de pytubefix de su prepo de github.
No me funciono descargar "highest resolution", 
me descarga el contenido en resoluciones inferiores como 360p, 
puede ser un bug de la dependencia o la forma en la que obtiene los streams.
"""

url = ""

yt = YouTube(url, on_progress_callback=on_progress)
print(yt.title)

ys = yt.streams.get_highest_resolution()
ys.download()