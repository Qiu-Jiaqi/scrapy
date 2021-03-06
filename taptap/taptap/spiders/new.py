# -*- coding: utf-8 -*-
import scrapy
import json
from taptap.items import NewItem
from bs4 import BeautifulSoup


# 新品榜
class NewSpider(scrapy.Spider):
    name = 'new'
    allowed_domains = ['www.taptap.com']
    start_urls = ['https://www.taptap.com/ajax/top/new?total=0&page=1']

    def parse(self, response):
        print(response.url)
        datas = json.loads(response.body)
        soup = BeautifulSoup(datas['data']['html'], 'lxml')
        for card in soup.select('body > div'):
            item = NewItem()
            item['top'] = card.select("span.top-card-order-text")[0].get_text()
            yield scrapy.Request(card.select('div.top-card-middle > a')[0].get('href'), self.parse_detail,
                                 meta={'item': item})
        next_url = datas['data']['next']
        if next_url:
            yield scrapy.Request(next_url)

    def parse_detail(self, response):
        print(response.url)
        item = response.meta['item']
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
