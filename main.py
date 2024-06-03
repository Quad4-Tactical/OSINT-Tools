from fastapi import FastAPI, BackgroundTasks, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse
from typing import Optional
from rss.rss_fetcher import fetch_rss_feed
from rss.fetch_fulltext import fetch_full_text
from translate.argos import translate_text
from ytdlp.download_video import download_video
from pydantic import BaseModel
import os
import uuid

app = FastAPI()
favicon_path = 'favicon.ico'

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/videos", StaticFiles(directory="videos"), name="videos")

class DownloadVideoRequest(BaseModel):
    url: str
    video_dir: Optional[str] = "videos"

class TranslateRequest(BaseModel):
    text: str
    from_lang: str
    to_lang: str

class FetchRSSRequest(BaseModel):
    feed_url: str
    full: Optional[bool] = False

downloads = {}

async def download_video_task(download_id, url, video_dir="videos"):
    video_info = download_video(url, video_dir)
    downloads[download_id] = os.path.basename(video_info)

@app.get("/")
async def read_root():
    return RedirectResponse(url='/static/index.html')

@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)

@app.post("/translate/")
def api_translate(request: TranslateRequest):
    return {"translated_text": translate_text(request.text, request.from_lang, request.to_lang)}

@app.post("/fetch-rss/")
def api_fetch_rss(request: FetchRSSRequest):
    articles = fetch_rss_feed(request.feed_url)
    if request.full:
        for article in articles:
            article['content'] = fetch_full_text(article['link'])
    return {"articles": articles}

@app.post("/download-video/")
async def api_download_video(request: DownloadVideoRequest, background_tasks: BackgroundTasks):
    download_id = str(uuid.uuid4())
    background_tasks.add_task(download_video_task, download_id, request.url, request.video_dir)
    return {"message": "Video download started.", "download_id": download_id}

@app.get("/check-download/{download_id}")
async def check_download(download_id: str):
    if download_id in downloads:
        video_path = downloads[download_id]
        video_filename = os.path.basename(video_path)
        return {"status": "completed", "video_url": f"/videos/{video_filename}"}
    return {"status": "downloading"}