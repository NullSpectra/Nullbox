import yt_dlp
import shutil
import sys
from pathlib import Path

path = Path.home() / "Downloads"

def check_ffmpeg():
    if shutil.which("ffmpeg") is None:
        print("Error: ffmpeg is not installed or not found in PATH.")
        print("Please install ffmpeg and add it to your system PATH.")
        input("Press Enter to exit...")
        sys.exit(1)

def download_video(url: str, chosen_format: str, output_path: Path = path):
    # output_path string olarak ve sonunda slash olmalı
    output_path_str = str(output_path)
    if not output_path_str.endswith(('/', '\\')):
        output_path_str += '/'

    ytdl_opts = {
        "outtmpl": output_path_str + '%(title)s.%(ext)s',
    }

    if chosen_format == "mp3":
        ytdl_opts.update({
            "format": "bestaudio/best",
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        })
    else:
        # MP4 için default formatı netleştir
        if chosen_format == 'mp4':
            ytdl_opts['format'] = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4'
        else:
            ytdl_opts['format'] = f'bestvideo[ext={chosen_format}]+bestaudio/best[ext={chosen_format}]/best[ext={chosen_format}]/best'

    with yt_dlp.YoutubeDL(ytdl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    check_ffmpeg()
    url = input("Enter video URL: ").strip()
    supported_formats = ['mp4', 'webm', 'mp3', 'm4a', 'wav']
    print("Supported formats:", supported_formats)
    chosen_format = input("Choose your format: ").strip().lower()
    if chosen_format not in supported_formats:
        print("Format not supported, defaulting to mp4.")
        chosen_format = 'mp4'

    download_video(url, chosen_format)
