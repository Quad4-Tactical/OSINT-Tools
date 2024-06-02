from bs4 import BeautifulSoup
import requests

def fetch_full_text(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.find_all(['p', 'h1', 'h2', 'h3'])

        full_text = '\n'.join([element.get_text() for element in content])
        return full_text
    except requests.RequestException as e:
        print(f"Error fetching full text from {url}: {e}")
        return ""