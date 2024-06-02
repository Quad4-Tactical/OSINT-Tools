import yt_dlp

def download_video(video_url, output_dir="."):
    """Download video from the given URL to the specified directory."""
    
    ydl_opts = {
        'paths': {'home': output_dir},
        'quiet': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Download video from URL using yt-dlp.')
    parser.add_argument('--url', help='Video URL to download', required=True)
    parser.add_argument('--dir', help='Directory to save the video', default='.')
    
    args = parser.parse_args()
    download_video(args.url, args.dir)