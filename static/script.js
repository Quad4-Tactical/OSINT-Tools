document.getElementById('translate-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    const text = document.getElementById('translate-text').value;
    const fromLang = document.getElementById('from-lang').value;
    const toLang = document.getElementById('to-lang').value;
    handleAction('/translate/', {text, from_lang: fromLang, to_lang: toLang});
});

document.getElementById('fetch-rss-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    const feedUrl = document.getElementById('rss-url').value;
    handleAction('/fetch-rss/', {feed_url: feedUrl});
});

document.getElementById('download-video-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    const videoUrl = document.getElementById('video-url').value;
    const response = await fetch('/download-video/', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({url: videoUrl})
    });
    const data = await response.json();
    checkDownloadStatus(data.download_id);
});

async function handleAction(url, data) {
    const response = await fetch(url, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    });
    const resultData = await response.json();
    displayResult(resultData);
}

function displayResult(data) {
    const container = document.getElementById('result-container');
    if (data.translated_text) {
        container.innerHTML = data.translated_text.replace(/\n/g, '<br>');
    } else if (data.articles) {
        displayRSS(data.articles);
    } else if (data.video_url) {
        displayVideo(data.video_url);
    } else {
        container.textContent = JSON.stringify(data, null, 2);
    }
}

function displayRSS(articles) {
    const container = document.getElementById('result-container');
    container.innerHTML = '';
    const list = document.createElement('ul');
    articles.forEach(article => {
        const item = document.createElement('li');

        const title = document.createElement('div');
        title.textContent = article.title;
        item.appendChild(title);

        const summary = document.createElement('p');
        summary.innerHTML = article.summary;
        item.appendChild(summary);

        const pubDate = document.createElement('span');
        pubDate.textContent = article.pubDate;
        item.appendChild(pubDate);

        if (article.link) {
            const link = document.createElement('a');
            link.setAttribute('href', article.link);
            link.textContent = 'Link';
            item.appendChild(link);
        }

        list.appendChild(item);
    });
    container.appendChild(list);
}


async function checkDownloadStatus(downloadId) {
    let statusResponse = await fetch(`/check-download/${downloadId}`);
    let statusData = await statusResponse.json();
    if (statusData.status === "completed") {
        displayVideo(statusData.video_url);
    } else {
        setTimeout(() => checkDownloadStatus(downloadId), 5000);
    }
}

function displayVideo(videoUrl) {
    let videoPlayer = document.createElement('video');
    videoPlayer.setAttribute('width', '320');
    videoPlayer.setAttribute('height', '240');
    videoPlayer.setAttribute('controls', '');

    let source = document.createElement('source');
    source.setAttribute('src', videoUrl);
    source.setAttribute('type', 'video/mp4');

    videoPlayer.appendChild(source);
    document.getElementById('result-container').appendChild(videoPlayer);
}
document.getElementById('copy-result-btn').addEventListener('click', function() {
    const textToCopy = document.getElementById('result-container').innerText;
    navigator.clipboard.writeText(textToCopy).then(() => {
        alert('Results copied to clipboard!');
    }).catch(err => {
        console.error('Error during copy: ', err);
    });
});

async function submitOCRForm(e) {
    e.preventDefault();

    const fileInput = document.getElementById('image-file');
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    try {
        const response = await fetch('/ocr/', {
            method: 'POST',
            body: formData
        });
        const data = await response.json();
        document.getElementById('result-container').textContent = data.extracted_text;
    } catch (error) {
        console.error('Error:', error);
    }
}