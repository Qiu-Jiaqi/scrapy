# -*- coding: utf-8 -*-
from taptap.items import GameItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


# 不断获取url进行爬取
class AllSpider(CrawlSpider):
    name = 'all'
    allowed_domains = ['www.taptap.com']
    start_urls = ['https://www.taptap.com/',
                  'https://www.taptap.com/top/download',
                  'https://www.taptap.com/review/new',
                  'https://www.taptap.com/categories',
                  'https://www.taptap.com/forum/hot',
                  'https://www.taptap.com/video']
    rules = [
        # follow=False(不跟进), 只提取首页符合规则的url，然后爬取这些url页面数据，callback解析
        # Follow=True(跟进链接), 在次级url页面中继续寻找符合规则的url,如此循环，直到把全站爬取完毕
        Rule(LinkExtractor(allow=r'/app/\d+$'), callback='parse_detail', follow=True)
    ]

    def parse_detail(self, response):
        print(response.url)
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
