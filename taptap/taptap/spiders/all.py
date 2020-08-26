# -*- coding: utf-8 -*-
import scrapy
import json
from taptap.items import GameItem
from scrapy.linkextractors import LinkExtractor


# 不断获取url进行爬取
class AllSpider(scrapy.Spider):
    name = 'all'
    allowed_domains = ['www.taptap.com']
    start_urls = ['https://www.taptap.com/'
                  'https://www.taptap.com/top/download',
                  'https://www.taptap.com/review/new',
                  'https://www.taptap.com/categories',
                  'https://www.taptap.com/forum/hot']

    def parse(self, response):
        print(response.url)
        link = LinkExtractor()
        links = link.extract_links(response)
        print(type(links))
        for link in links:
            print(link)
