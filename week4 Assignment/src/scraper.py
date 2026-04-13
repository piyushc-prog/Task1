import requests
from bs4 import BeautifulSoup

class ArticleScraper:
    def fetch_article(self, url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            paragraphs = soup.find_all('p')
            text = " ".join([p.get_text() for p in paragraphs])
            
            return text
        
        except Exception as e:
            print("Error:", e)
            return ""