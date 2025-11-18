from dataclasses import dataclass           # Para crear una clase
from pytubefix import YouTube, Playlist     # Para descargar videos y PlayList de YouTube
from pytubefix.cli import on_progress       # Para mostrar el progreso de descarga
from re import match as re_match            # Para detectar enlaces de YouTube


# CONSTS
MAX_DOWNLOAD_SIZE: float = 30 # per file MegaBytes (MB)
PATTERN: str = r'(https?://)?(www\.)?(music\.)?(youtube\.com|youtu\.be)/.+'

download_path: str


@dataclass
class Song:
    title: str
    author: str
    downloaded: bool
    size: float

def print_details(song: Song):
    print("Downloaded Song:")
    print("Title:  " + song.title)
    print("Author: " + song.author)
    print("Size:   " + str(song.size) + " MB")
    print("- - - - -")

    
def is_youtube_link(url) -> bool:
    #return True
    if re_match(PATTERN, url):
        return True
    
    return False

def clean_video_author(title: str) -> str:
    if " - Topic" in title:
        title = title.replace(" - Topic", "")
    
    return title

def download_playlist(url: str) -> bool:
    playlist: Playlist = Playlist(url=url)
    try:
        for video in playlist.videos:
            #if video.streams.get_audio_only().filesize_mb > MAX_DOWNLOAD_SIZE:
            #    continue

            download_song(
                YouTube(
                video.watch_url,
                on_progress_callback=on_progress)
                )
        
        return True
    except Exception as e:
        print(f"error on downloding playlist: {e}")
        return False


# Only one audio
def download_song(video: YouTube) -> bool:
    title: str = video.title
    author: str = clean_video_author(video.author)
    size: float = video.streams.get_audio_only().filesize_mb #type:ignore

    video.streams.get_audio_only().download(
            filename=f"{video.title}.mp3",
            output_path=download_path,  # my download folder path
            skip_existing=False,        # overwrite?
            max_retries=3)              # Retrys

    song: Song = Song(title, author, True, size)
    print_details(song=song)



def Download(yt_url: str) -> bool:
    if "list=" in yt_url.lower():
       return download_playlist(yt_url)
    else:
        return download_song(yt_url)


def validate_download_path(path: str) -> bool:
    import os
    expanded_path = os.path.expanduser(path)
    if os.path.exists(expanded_path) and os.path.isdir(expanded_path):
        global download_path
        download_path = expanded_path
        return True
    else:
        print("The specified download path does not exist or is not a directory.")
        return False



if __name__ == "__main__":
    import sys
    print("Select download path: (optional, default = ~/Music)")
    path_input = str(input("Path: ") or "~/Music")
    if not validate_download_path(path_input):
        sys.exit(1)
        
    print("Enter YouTube link (video or playlist):")
    youtube_link: str = str(input("Link: "))
    if not is_youtube_link(youtube_link):
        print("The provided link is not a valid YouTube URL.")
        sys.exit(1)
    
    Download(youtube_link)
