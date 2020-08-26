# -*- coding: utf-8 -*-
import scrapy
import json
from taptap.items import SoleItem
from bs4 import BeautifulSoup


# taptap独家
class SoleSpider(scrapy.Spider):
    name = 'sole'
    allowed_domains = ['www.taptap.com']
    start_urls = ['https://www.taptap.com/ajax/search/tags?&kw=taptap%E7%8B%AC%E5%AE%B6&sort=hits&page=1']

    def parse(self, response):
        print(response.url)
        datas = json.loads(response.body)
        soup = BeautifulSoup(datas['data']['html'], 'lxml')
        for card in soup.select('body > div'):
            yield scrapy.Request(card.select('a')[0].get('href'), self.parse_detail)
        next_url = datas['data']['next']
        if next_url:
            yield scrapy.Request(next_url)

    def parse_detail(self, response):
        print(response.url)
        item = SoleItem()
        item['id'] = response.url.split('/')[-1]
        item['name'] = response.xpath(
            '//*[@id="js-nav-sidebar-main"]/div[1]/div/div/section[1]/div[1]/div[2]/div[1]/h1/text()'). \
            extract()[0].strip()
        item['author'] = response.xpath(
            '//*[@id="js-nav-sidebar-main"]/div[1]/div/div/section[1]/div[1]/div[2]/div[1]/div/a/span[2]/text()'). \
            extract()[0].strip()
        rating = response.xpath(
            '//*[@id="js-nav-sidebar-main"]/div[1]/div/div/section[1]/div[1]/div[2]/div[1]/span/span/span/text()')
        if rating:
            item['rating'] = rating.extract()[0]
        else:
            item['rating'] = "评分过少"
        tags = []
        for sel in response.xpath('//*[@id="appTag"]/li'):
            tag = sel.xpath('a/text()')
            if tag:
                tags.append(tag.extract()[0].strip())
        item['tags'] = ",".join(tags)
        print(item['tags'])
        item['category'] = \
            response.xpath('//*[@id="js-nav-sidebar-main"]/section[1]/div/div/ol/li[3]/a/text()').extract()[0]
        yield item
