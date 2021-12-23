import requests
import os
from bs4 import BeautifulSoup

site = requests.get('https://www.detik.com/terpopuler?')

params = {
    'tag_from': 'wp_cb_mostPopular_more'
}

try:
    os.mkdir('temp')
except FileExistsError:
    pass

with open('temp/res.html', 'w+') as outfile:
    outfile.write(site.text)
    outfile.close()

soup = BeautifulSoup(site.text, 'html.parser')

populer_news = soup.find(attrs={'class', 'grid-row list-content'})

title = populer_news.find_all(attrs={'class', 'media__title'})
images = populer_news.find_all(attrs={'class', 'media__image'})

for i in images:
    print(i.find('a').find('img')['title'])


# print(title)

