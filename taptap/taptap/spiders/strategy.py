# -*- coding: utf-8 -*-
import scrapy
import json
from taptap.items import StrategyItem
from bs4 import BeautifulSoup


# 策略游戏
class StrategySpider(scrapy.Spider):
    name = 'strategy'
    allowed_domains = ['www.taptap.com']
    start_urls = ['https://www.taptap.com/ajax/search/tags?&kw=%E7%AD%96%E7%95%A5&sort=hits&page=1']

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
        item = StrategyItem()
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
        flag = response.css(
            '#js-nav-sidebar-main > div.container.app-main-container > div > div > section.app-show-main.taptap-page-main > div.show-main-header > div.main-header-text > div.header-text-download > div.text-download-text p > span::text') \
            .extract()
        if len(flag) == 2:
            item['install_num'] = flag[0].split(' ')[0]
            item['follow_num'] = flag[1].split(' ')[0]
        elif len(flag) == 1:
            item['install_num'] = 0
            item['follow_num'] = flag[0].split(' ')[0]
        else:
            item['install_num'] = 0
            item['follow_num'] = 0
        yield item
