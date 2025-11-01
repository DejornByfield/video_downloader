import yt_dlp
import os 
from flask import current_app

def download_video(url):
    output_folder = current_app.config['DOWNLOAD_FOLDER']
    ydl_opts = {
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'noplaylist': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        return {
                'title': info.get('title'),
                'filepath': filename,
                'filesize': info.get('filesize', 0),
        }
