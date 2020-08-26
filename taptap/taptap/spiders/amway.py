# -*- coding: utf-8 -*-
import scrapy
import json
from taptap.items import AmwayItem
from bs4 import BeautifulSoup


# 安利墙
class AmwaySpider(scrapy.Spider):
    name = 'amway'
    allowed_domains = ['www.taptap.com']
    start_urls = ['https://www.taptap.com/ajax/review/new']

    def parse(self, response):
        print(response.url)
        datas = json.loads(response.body)
        soup = BeautifulSoup(datas['data']['html'], 'lxml')
        for card in soup.select('body > div'):
            yield scrapy.Request(card.select('div.review-block-app > a')[0].get('href'), self.parse_detail)
        next_url = datas['data']['next']
        if next_url:
            yield scrapy.Request(next_url)

    def parse_detail(self, response):
        print(response.url)
        item = AmwayItem()
        item['id'] = response.url.split('/')[-1]
        item['name'] = response.xpath(
            '//*[@id="js-nav-sidebar-main"]/div[1]/div/div/section[1]/div[1]/div[2]/div[1]/h1/text()').extract_first().strip()
        item['author'] = response.xpath(
            '//*[@id="js-nav-sidebar-main"]/div[1]/div/div/section[1]/div[1]/div[2]/div[1]/div/a/span[2]/text()').extract_first().strip()
        rating = response.xpath(
            '//*[@id="js-nav-sidebar-main"]/div[1]/div/div/section[1]/div[1]/div[2]/div[1]/span/span/span/text()')
        if rating:
            item['rating'] = rating.extract_first()
        else:
            item['rating'] = "评分过少"
        tags = response.css('#appTag > li > a::text').extract()
        tags = list(map(str.strip, tags))
        item['tags'] = ','.join(tags)
        item['category'] = \
            response.xpath('//*[@id="js-nav-sidebar-main"]/section[1]/div/div/ol/li[3]/a/text()').extract_first()
        yield item
