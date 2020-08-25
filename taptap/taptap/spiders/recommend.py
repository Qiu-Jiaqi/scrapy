# -*- coding: utf-8 -*-
import scrapy
from taptap.items import RecommendItem


# 发现-往期推荐
class RecommendSpider(scrapy.Spider):
    name = 'recommend'
    allowed_domains = ['www.taptap.com']
    start_urls = ['https://www.taptap.com/category/recommend?sort=hits&page=1']

    def parse(self, response):
        print(response.url)
        if len(response.xpath('//*[@id="js-nav-sidebar-main"]/div[1]/div[1]/div/section/div[2]/div')) == 0:
            return
        for item in response.xpath('//*[@id="js-nav-sidebar-main"]/div[1]/div[1]/div/section/div[2]/div'):
            yield scrapy.Request(item.xpath('a/@href').extract()[0], self.parse_detail)
        page = int(response.url.split('=')[-1])
        page += 1
        next_url = response.url.split('page')[0] + "page=" + str(page)
        yield scrapy.Request(next_url)

    def parse_detail(self, response):
        print(response.url)
        item = RecommendItem()
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
        item['category'] = \
            response.xpath('//*[@id="js-nav-sidebar-main"]/section[1]/div/div/ol/li[3]/a/text()').extract()[0]
        yield item
