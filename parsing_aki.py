from bs4 import BeautifulSoup
import requests

url = "https://akipress.org/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('a', class_='newslink')
n = 0
for news in quotes:
    n += 1
    # print(f"{n}) {news.text}\n")
    with open('news.txt', 'a+', encoding='utf-8') as aki:
        aki.write(f"{n}) {news.text}\n")