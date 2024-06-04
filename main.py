from fastapi import FastAPI, BackgroundTasks, HTTPException, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from rss.rss_fetcher import fetch_rss_feed
from rss.fetch_fulltext import fetch_full_text
from translate.argos import translate_text
from ytdlp.download_video import download_video 
from ocr.ocr import perform_ocr
from pydantic import BaseModel
import os
import uuid
import shutil
import yaml

tags_metadata = [
    {
        "name": "Translate",
        "description": "Translation-related operations. Convert text between languages.",
    },
    {
        "name": "RSS",
        "description": "RSS feed fetching. Obtain and optionally fetch full article content.",
    },
    {
        "name": "Video Download",
        "description": "Video download operations. Download videos from various sources.",
    },
    {
        "name": "OCR",
        "description": "Optical Character Recognition. Extract text from images.",
    },
]

app = FastAPI(
    title="OSINT Tools",
    openapi_tags=tags_metadata,
)

with open('config.yml', 'r') as f:
    config = yaml.safe_load(f)

app.add_middleware(
    CORSMiddleware,
    **config['cors_config']
)

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

async def download_video_task(download_id, url, config, video_dir="videos"):
    video_info = download_video(url, config, video_dir)
    downloads[download_id] = os.path.basename(video_info)

@app.get("/")
async def read_root():
    return RedirectResponse(url='/static/index.html')

@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)

@app.post("/translate/", tags=["Translate"])
def api_translate(request: TranslateRequest):
    return {"translated_text": translate_text(request.text, request.from_lang, request.to_lang, config)}

@app.post("/ocr/", tags=["OCR"])
async def ocr_endpoint(file: UploadFile = File(...)):
    temp_file_path = f"temp_{uuid.uuid4().hex}.jpg"
    with open(temp_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    extracted_text = perform_ocr(temp_file_path)
    return {"extracted_text": extracted_text}

@app.post("/fetch-rss/", tags=["RSS"])
def api_fetch_rss(request: FetchRSSRequest):
    articles = fetch_rss_feed(request.feed_url)
    if request.full:
        for article in articles:
            article['content'] = fetch_full_text(article['link'])
    return {"articles": articles}

@app.post("/download-video/", tags=["Video Download"])
async def api_download_video(request: DownloadVideoRequest, background_tasks: BackgroundTasks):
    download_id = str(uuid.uuid4())
    background_tasks.add_task(download_video_task, download_id, request.url, config, request.video_dir)
    return {"message": "Video download started.", "download_id": download_id}

@app.get("/check-download/{download_id}")
async def check_download(download_id: str):
    if download_id in downloads:
        video_path = downloads[download_id]
        video_filename = os.path.basename(video_path)
        return {"status": "completed", "video_url": f"/videos/{video_filename}"}
    return {"status": "downloading"}