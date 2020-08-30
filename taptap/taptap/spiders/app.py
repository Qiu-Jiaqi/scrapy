# -*- coding: utf-8 -*-
import scrapy
from taptap.items import GameItem


# 不断获取app
class AppSpider(scrapy.Spider):
    name = 'app'
    allowed_domains = ['www.taptap.com']
    start_urls = ['https://www.taptap.com/app/1']

    def parse(self, response):
        print(response.url)
        for i in range(1, 200000):
            print(i)
            url = response.url[:-1] + str(i)
            yield scrapy.Request(url, self.parse_detail)

    def parse_detail(self, response):
        print(response.url)
        if response.css('#taptap-error-title'):
            return
        item = GameItem()
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
