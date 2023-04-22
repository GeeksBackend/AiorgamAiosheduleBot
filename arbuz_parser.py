import asyncio
import aiohttp
from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent
from pyshorteners import Shortener
import ssl

BASE_URL="https://arbuz.kz/ru/collections/249002-chai_kofe_so_skidkoi_do_30_#/"
HEADERS = {"User-Agent":UserAgent().random}

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL, headers=HEADERS, ssl=False) as response:
            r = await response.content.read()
            soup = BS(r,'html.parser')
            items = soup.find_all('article',{'class':'product-item product-card'})
            shortener = Shortener(timeout=5)
            for item in items:
                title = item.find('a',{'class':'product-card__title'})
                link = title.get('href')
                price = item.find('b').text.split()
                short_price = shortener.tinyurl.short(f'https://arbuz.kz{link}')
                print(f'TITLE:{title.text} | {price} | {short_price}')

if __name__ =='__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())