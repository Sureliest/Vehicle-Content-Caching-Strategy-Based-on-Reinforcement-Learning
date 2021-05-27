import scrapy
from DouBanTop.items import DoubantopItem
import requests
import re

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    start_urls = ['https://movie.douban.com/chart']

    def parse(self, response):
        url_list=response.xpath('//*[@id="content"]/div/div[2]/div[1]/div[@class="types"]/span/a/@href').extract()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4343.0 Safari/537.36'
        }
        post_url = 'https://movie.douban.com/j/chart/top_list'
        for url in url_list:
            movie_page='.*?&type=(.*?)&interval.*?'
            movie_type_name='.*?type_name=(.*?)&type=.*?'
            movie_type = re.findall(movie_page,url,re.S)[0]
            type_name = re.findall(movie_type_name,url,re.S)[0]
            print(movie_type, type_name)
            param = {
                'type': movie_type,
                'interval_id': '100:90',
                'action': '',
                'start': '0',
                'limit': '50',
            }
            page_data = requests.get(url=post_url, params=param, headers=headers)
            list_data = page_data.json()
            for i in range(0, 50):
                item = DoubantopItem()
                item['rank'] = list_data[i]['rank']
                item['title'] = list_data[i]['title']
                item['release_date'] = list_data[i]['release_date']
                regions=""
                for region in list_data[i]['regions']:
                    regions=regions+region+"/"
                item['regions'] = regions
                item['score'] = list_data[i]['score']
                item['type'] = type_name
                yield item
