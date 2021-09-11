import requests
from urllib import parse
from bs4 import BeautifulSoup

class News:
    def __init__(self, title: str, media: str, time_ago: str, url: str) -> None:
        self.title = title
        self.media = media
        self.time_ago = time_ago
        self.url = 'https://news.google.com/' + url[2:]
    
    def __str__(self) -> str:
        return f'{self.title}, {self.media}, {self.time_ago},\n{self.url}'

class TopTenNews:
    def __init__(self, keyword: str) -> None:
        news_url: str = f'https://news.google.com/search?q={parse.quote(keyword)}&hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant'
        response = requests.get(news_url)
        self.news: News = []
        self.news_count: int = 0
        soup = BeautifulSoup(response.text, 'html.parser')

        titles = soup.find_all('a', class_='DY5T1d')
        medias = soup.find_all('a', class_='wEwyrc AVN2gc uQIVzc Sksgp')
        timeAgos = soup.find_all('time', class_='WW6dff uQIVzc Sksgp')

        i = 0
        while i < 10:
            try:
                self.news.append(News(titles[i].text, medias[i].text, timeAgos[i].text, titles[i]['href']))
                i += 1
            except:
                break
        self.news_count = i
        
if __name__ == '__main__':
    news_obj = TopTenNews('qew')
    for news in news_obj.news :
        print(news.title, news.media, news.time_ago)
    print('')
    print('新聞數:', news_obj.news_count)
