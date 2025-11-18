# Descargador de Canciones de YouTube

Un pequeño script en Python que descarga canciones de YouTube.

Traté de hacerlo lo más simple posible agregando algunas validaciones y limitaciones.

Solo pide una ruta opcional de descarga y un enlace de YouTube (video o playlist).

## Notas:
- La ruta de descarga por defecto es ~/Music
- Solo descarga archivos de hasta 30 MB (MAX_DOWNLOAD_SIZE)
- Solo acepta enlaces de YouTube y YouTube Music (PATTERN)
- Algunas canciones de YT Music suelen tener menor calidad que las de YT normal usando este script.

## Instalación

1. Instala Python 3.x si no lo tienes.
2. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    # alternativa
    python -m pip install pytubefix
    ```

## Uso

Ejecuta el script:

```bash
python main.py
```

Sigue las instrucciones para ingresar la ruta de descarga (opcional) y el enlace de YouTube.

## Autor

Script por aaron-dotnet