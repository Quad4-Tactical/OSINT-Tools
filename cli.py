import argparse
import csv
from rss.rss_fetcher import fetch_rss_feed
from rss.fetch_fulltext import fetch_full_text
from translate.argos import translate_text

def translate_file(filename, from_lang, to_lang):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    translated_content = translate_text(content, from_lang, to_lang)
    new_filename = f"{filename.rsplit('.', 1)[0]}_translated.txt"
    with open(new_filename, 'w', encoding='utf-8') as f:
        f.write(translated_content)

def export_to_markdown(articles, filename, from_lang=None, to_lang=None):
    with open(filename, 'w', encoding='utf-8') as f:
        for article in articles:
            title = article['title']
            link = article['link']
            content = fetch_full_text(link)
            if from_lang and to_lang:
                title = translate_text(title, from_lang, to_lang)
                content = translate_text(content, from_lang, to_lang)
            f.write(f"# {title}\n\n")
            f.write(f"[Link]({link})\n\n")
            f.write(f"{content}\n\n---\n\n")

def export_to_txt(articles, filename, from_lang=None, to_lang=None):
    with open(filename, 'w', encoding='utf-8') as f:
        for article in articles:
            title = article['title']
            link = article['link']
            content = fetch_full_text(link)
            if from_lang and to_lang:
                title = translate_text(title, from_lang, to_lang)
                content = translate_text(content, from_lang, to_lang)
            f.write(f"Title: {title}\n")
            f.write(f"Link: {link}\n")
            f.write(f"Content: {content}\n---\n\n")

def export_to_csv(articles, filename, from_lang=None, to_lang=None):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Link", "Content"])
        for article in articles:
            title = article['title']
            link = article['link']
            content = fetch_full_text(link)
            if from_lang and to_lang:
                title = translate_text(title, from_lang, to_lang)
                content = translate_text(content, from_lang, to_lang)
            writer.writerow([title, link, content])

def main():
    parser = argparse.ArgumentParser(description="Utility for translating text, files, and RSS feed articles.")
    parser.add_argument("--translate", help="Text to translate directly.")
    parser.add_argument("--translate-file", help="Path to a file to translate.")
    parser.add_argument("--feed-url", help="RSS feed URL to fetch and translate articles.")
    parser.add_argument("--full", action="store_true", help="Fetch full text content for each article.")
    parser.add_argument("--export", choices=['markdown', 'txt', 'csv'], help="Export format for translated RSS articles.")
    parser.add_argument("--output", default="exported_articles", help="Output file name (without extension) for exported RSS articles.")
    parser.add_argument("--from-lang", required=True, help="Source language code.")
    parser.add_argument("--to-lang", required=True, help="Target language code.")
    args = parser.parse_args()

    if args.translate:
        print(translate_text(args.translate, args.from_lang, args.to_lang))
    elif args.file:
        translate_file(args.file, args.from_lang, args.to_lang)
    elif args.feed_url:
        articles = fetch_rss_feed(args.feed_url)
        if args.export and args.full:
            export_func = export_to_markdown if args.export == "markdown" else export_to_txt if args.export == "txt" else export_to_csv
            export_func(articles, f"{args.output}.{args.export}", args.from_lang, args.to_lang)
        else:
            for article in articles:
                title = translate_text(article['title'], args.from_lang, args.to_lang)
                print(f"Title: {title}\nLink: {article['link']}\n---")
        
if __name__ == "__main__":
    main()
