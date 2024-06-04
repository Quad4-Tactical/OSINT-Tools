import yt_dlp
import os
import secrets

def download_video(video_url, output_dir="videos"):
    random_filename = secrets.token_hex(4)
    
    ydl_opts = {
        'outtmpl': os.path.join(output_dir, f'{random_filename}.%(ext)s'),
        'quiet': True,
        'embed-thumbnail': True,
        'embed-metadata': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=True)
        video_ext = info_dict.get('ext')
        video_filename = f"{random_filename}.{video_ext}"
        video_path = os.path.join(output_dir, video_filename)
        
    return os.path.abspath(video_path)