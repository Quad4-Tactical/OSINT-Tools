import feedparser

def fetch_rss_feed(feed_url):
    parsed_feed = feedparser.parse(feed_url)
    articles = []

    for entry in parsed_feed.entries:
        article = {
            'title': entry.title,
            'link': entry.link,
            'published': entry.get('published', 'No date available'),
            'summary': entry.get('summary', 'No summary available')
        }
        articles.append(article)
    
    return articles