import sys
sys.path.append('D:\\python_packages')

import requests
from bs4 import BeautifulSoup

def scrape_news():
    # rest of code...scrape_news():
    url = "https://news.ycombinator.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    stories = soup.find_all('span', class_='titleline')[:5]
    
    print("=== Top 5 Stories ===\n")
    for i, story in enumerate(stories, 1):
        link = story.find('a')
        if link:
            print(f"{i}. {link.text}")
            print(f"   URL: {link['href']}\n")

scrape_news()
